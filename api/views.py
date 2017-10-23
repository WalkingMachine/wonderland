from api.models import Entity, Human, Object, Room, Waypoint, ArTag
from api.serializers import EntitySerializer, HumanSerializer
from api.serializers import ObjectSerializer, RoomSerializer
from api.serializers import WaypointSerializer, ArTagSerializer
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
        name = request.query_params.get('name', None)
        color = request.query_params.get('color', None)
        room = request.query_params.get('room', None)
        type = request.query_params.get('type', None)
        id = request.query_params.get('id', None)

        objects = Object.objects.all()
        if name is not None:
            objects = objects.filter(name__icontains=str(name))
        if color is not None:
            objects = objects.filter(color__icontains=str(color))
        if room is not None:
            objects = objects.filter(room__room_name__icontains=str(room))
        if type is not None:
            objects = objects.filter(type__icontains=str(type))
        if id is not None:
            objects = objects.filter(id__exact=id)

        #objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomList(APIView):

    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WaypointList(APIView):

    def get(self, request, format=None):
        waypoints = Waypoint.objects.all()
        serializer = WaypointSerializer(waypoints, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WaypointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArTagList(APIView):

    def get(self, request, format=None):
        artag = ArTag.objects.all()
        serializer = ArTagSerializer(artag, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
