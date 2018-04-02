from api.models import Entity, Space
from api.serializers import EntitySerializer, SpaceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EntityList(APIView):

    # List all Entity or create a new entity.
    def get(self, request, format=None):
        entities = Entity.objects.all()
        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpaceList(APIView):
    # List all Entity or create a new entity.
    def get(self, request, format=None):
        objects = Space.objects.all()

        # Read parameters
        space_id = request.query_params.get('space_id', None)
        name = request.query_params.get('name', None)
        x_position = request.query_params.get('x_position', None)
        y_position = request.query_params.get('y_position', None)

        if space_id is not None:
            # If there is an ID parameter, return the corespondent rooms
            objects = objects.filter(space_id__exact=space_id)

        elif name is not None:
            # If there is a name parameter, return the corespondent rooms
            objects = objects.filter(name__icontains=str(name))

        elif x_position is not None and y_position is not None:
            # If there is position parameters, return the rooms corresponding to the position
            objects = objects.filter(x_left__lte=x_position,
                                     x_right__gte=x_position,
                                     y_top__gte=y_position,
                                     y_bottom__lte=y_position)

        serializer = SpaceSerializer(objects, many=True)

        return Response(serializer.data)

    # Add a room in the arena
    def post(self, request, format=None):
        serializer = SpaceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)