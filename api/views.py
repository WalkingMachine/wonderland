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
        entity_container = request.query_params.get('entityContainer', None)
        entity_room = request.query_params.get('entityRoom', None)
        entity_id = request.query_params.get('entityId', None)

        if entity_id is not None:
            print "ID:" + entity_id
            objects = objects.filter(entityId__iexact=str(entity_id))

        else:
            # Filter by asked class
            if entity_class is not None:
                print "class"
                objects = objects.filter(entityClass__iexact=str(entity_class))

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
                    Q(Q(entityContainer__entityClass__iexact=str(entity_room)),
                      Q(entityContainer__entityIsRoom__exact=True)) |
                    Q(Q(entityContainer__entityContainer__entityClass__iexact=str(entity_room)),
                      Q(entityContainer__entityContainer__entityIsRoom__exact=True)) |
                    Q(Q(entityContainer__entityContainer__entityContainer__entityClass__iexact=str(entity_room)),
                      Q(entityContainer__entityContainer__entityContainer__entityIsRoom__exact=True))
                )

        serializer = EntitySerializer(objects, many=True)
        return Response(serializer.data)

    # Add a room in the arena
    def post(self, request, format=None):
        # TODO: ADD THIS PART
        data = request.data

        if not data._mutable:
            data._mutable = True

        serializer = EntitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
