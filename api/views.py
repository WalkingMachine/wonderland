from api.models import Entity
from api.serializers import EntitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EntityList(APIView):

    ''' List all Entity or create a new entity. '''

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
