from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Entity, People
from serializers import EntitySerializer, PeopleSerializer


class EntityList(APIView):
    # List all entity
    @staticmethod
    def get(request):
        objects = Entity.objects.all()
        entity_class = request.query_params.get('entityClass', None)
        entity_category = request.query_params.get('entityCategory', None)
        entity_containers = request.query_params.getlist('entityContainer')
        entity_id = request.query_params.get('entityId', None)
        depth_limit = request.query_params.get('depthLimit', 3)

        if entity_id is not None:
            objects = objects.filter(entityId__iexact=str(entity_id))

        else:
            # Filter by asked class
            if entity_class is not None:
                objects = objects.filter(entityClass__icontains=str(entity_class))

            # Filter by asked category
            if entity_category is not None:
                objects = objects.filter(entityCategory__icontains=str(entity_category))

            # Filter by asked containers
            for entity_container in entity_containers:
                objects = objects.filter(
                    Q(entityContainer__entityClass__icontains=str(entity_container)) |
                    Q(entityContainer__entityContainer__entityClass__icontains=str(entity_container)) |
                    Q(entityContainer__entityContainer__entityContainer__entityClass__icontains=str(entity_container)))

        if len(objects) <= 0:
            serializer = EntitySerializer(None, many=True)
            return Response(serializer.data)

        # For all object after filter
        for anObject in objects:
            next_object = anObject
            depth = 0
            anObject.depth_waypoint = None
            anObject.depth_position = None

            # Find the first parent with a waypoint and the first parent with a location.
            while depth <= depth_limit and (anObject.depth_waypoint is None or anObject.depth_position is None):

                # Save the first and only the first waypoint location
                if (next_object.entityWaypointX is not None
                        and next_object.entityWaypointY is not None
                        and anObject.depth_waypoint is None):
                    anObject.depth_waypoint = depth
                    anObject.entityWaypointX = next_object.entityWaypointX
                    anObject.entityWaypointY = next_object.entityWaypointY
                    anObject.entityWaypointYaw = next_object.entityWaypointYaw

                # Save the first and only the first object location
                if (next_object.entityPosX is not None
                        and next_object.entityPosY is not None
                        and anObject.depth_position is None):
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

    # Add an entity in the arena
    @staticmethod
    def post(request):

        # TODO add a verbal selection for container, instead of use ID.

        data = request.data

        if hasattr(data, '_mutable') and not data._mutable:
            data._mutable = True

        serializer = EntitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleList(APIView):
    # List all peoples
    @staticmethod
    def get(request):
        objects = People.objects.all()

        people_id = request.query_params.get('peopleId', None)
        people_recognition_id = request.query_params.get('peopleRecognitionId', None)
        people_color = request.query_params.get('peopleColor', None)
        people_pose = request.query_params.get('peoplePose', None)
        people_gender = request.query_params.get('peopleGender', None)

        if people_id is not None:
            objects = objects.filter(peopleId__iexact=people_id)

        else:
            # Filter by asked class
            if people_recognition_id is not None:
                objects = objects.filter(peopleRecognitionId__iexact=people_recognition_id)
            if people_color is not None:
                objects = objects.filter(peopleColor__icontains=people_color)
            if people_pose is not None:
                objects = objects.filter(peoplePose__icontains=people_pose)
            if people_gender is not None:
                objects = objects.filter(peopleGender__icontains=people_gender)

        serializer = PeopleSerializer(objects, many=True)
        return Response(serializer.data)

    # Add a people in the arena
    @staticmethod
    def post(request):
        data = request.data

        if hasattr(data, '_mutable') and not data._mutable:
            data._mutable = True

        serializer = PeopleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
