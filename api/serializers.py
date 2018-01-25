from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Human, Object, Room, Waypoint, ArTag


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id','name', 'time', 'x_position', 'y_position', 'z_position')


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ('id','name', 'gender', 'x_position', 'y_position', 'z_position')


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('id', 'name', 'type', 'color', 'room',  'x_position', 'y_position', 'z_position', 'theta')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id', 'name', 'type',  'x_position', 'y_position', 'z_position'
        )


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ('id', 'name', 'x_position', 'y_position')


class ArTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArTag
        fields = ('id', 'name', 'ar_id',  'x_position', 'y_position', 'z_position', 'theta')
