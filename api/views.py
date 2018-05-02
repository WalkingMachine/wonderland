from .models import Entity
from .serializers import EntitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class EntityList(APIView):
    # List all Entity or create a new entity.
    def get(self, request, format=None):
        objects = Entity.objects.all()
        entity_class = request.query_params.get('entityClass', None)
        entity_category = request.query_params.get('entityCategory', None)
        entity_container = request.query_params.get('entityContainer', None)
        entity_room = request.query_params.get('entityRoom', None)
        entity_id = request.query_params.get('entityId', None)
        depth_limit = request.query_params.get('depthLimit', 3)

        if entity_id is not None:
            print "ID:" + entity_id
            objects = objects.filter(entityId__iexact=str(entity_id))

        else:
            # Filter by asked class
            if entity_class is not None:
                print "class"
                objects = objects.filter(entityClass__iexact=str(entity_class))

            # Filter by asked category
            if entity_category is not None:
                print "category"
                objects = objects.filter(entityCategory__iexact=str(entity_category))

            # Filter by asked container
            if entity_container is not None:
                print "container"
                objects = objects.filter(
                    Q(entityContainer__entityClass__iexact=str(entity_container)) |
                    Q(entityContainer__entityContainer__entityClass__iexact=str(entity_container)) |
                    Q(entityContainer__entityContainer__entityContainer__entityClass__iexact=str(entity_container)))

            # Filter by asked room
            if entity_room is not None:
                print "room"
                objects = objects.filter(
                    Q(entityContainer__entityClass__iexact=str(entity_room)) |
                    Q(entityContainer__entityContainer__entityClass__iexact=str(entity_room)) |
                    Q(entityContainer__entityContainer__entityContainer__entityClass__iexact=str(entity_room))
                )

        if len(objects) <= 0:
            serializer = EntitySerializer(None, many=True)
            return Response(serializer.data)

        # For all object after filter
        for anObject in objects:
            next_object = anObject
            depth = 0
            anObject.depth_waypoint = None
            anObject.depth_position = None

            # Find the first parent with a waypoint and the first parent with a geolocation.
            while depth <= depth_limit and (anObject.depth_waypoint is None or anObject.depth_position is None):

                # Save the first and only the first waypoint location
                if next_object.entityIsWaypoint and anObject.depth_waypoint is None:
                    anObject.depth_waypoint = depth
                    anObject.entityWaypointX = next_object.entityWaypointX
                    anObject.entityWaypointY = next_object.entityWaypointY
                    anObject.entityWaypointYaw = next_object.entityWaypointYaw

                # Save the first and only the first object location
                if next_object.entityGotPosition and anObject.depth_position is None:
                    anObject.depth_position = depth
                    anObject.entityPosX = next_object.entityPosX
                    anObject.entityPosY = next_object.entityPosY
                    anObject.entityPosZ = next_object.entityPosZ
                    anObject.entityPosYaw = next_object.entityPosYaw
                    anObject.entityPosPitch = next_object.entityPosPitch
                    anObject.entityPosRoll = next_object.entityPosRoll

                # If there is no more parent, stop the loop
                if next_object.entityContainer is None or next_object.entityIsRoom:
                    break

                # For limit the loop in error case
                next_object = next_object.entityContainer
                depth += 1

        if entity_id is not None:
            serializer = EntitySerializer(objects[0], many=False)
        else:
            serializer = EntitySerializer(objects, many=True)

        return Response(serializer.data)

    # Add a room in the arena
    def post(self, request, format=None):

        # TODO add a verbal selection for container, instead of use ID.

        data = request.data

        if not data._mutable:
            data._mutable = True

            # For object position
            entity_pos_x = data['entityPosX'] if 'entityPosX' in data else None
            entity_pos_y = data['entityPosY'] if 'entityPosY' in data else None
            entity_pos_z = data['entityPosZ'] if 'entityPosZ' in data else None

            data['entityGotPosition'] = (entity_pos_x is not None and
                                         entity_pos_y is not None and
                                         entity_pos_z is not None)

            # For waypoint
            entity_waypoint_x = data['entityWaypointX'] if 'entityWaypointX' in data else None
            entity_waypoint_y = data['entityWaypointY'] if 'entityWaypointY' in data else None

            data['entityIsWaypoint'] = (entity_waypoint_x is not None and
                                        entity_waypoint_y is not None)

        serializer = EntitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
