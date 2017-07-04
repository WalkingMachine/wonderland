from api.models import Entity, Human, Object
from api.serializers import EntitySerializer, HumanSerializer, ObjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import manage as main


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


class HumanList(APIView):
    ''' List all Human. '''

    def get(self, request, format=None):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObjectList(APIView):
    ''' List all Object. '''

    def get(self, request, format=None):
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
