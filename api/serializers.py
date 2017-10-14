from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Human, Object, Room, Waypoint, ArTag


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('name', 'time', 'x_position', 'y_position', 'z_position')


class HumanSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Human
        fields = ('entity', 'gender', 'person_name')


class ObjectSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Object
        fields = ('entity', 'type', 'color')


class RoomSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Room
        fields = (
            'entity''x1', 'x2', 'x3', 'x4', 'y1', 'y2', 'y3', 'y4', 'room_name'
        )


class WaypointSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Waypoint
        fields = ('entity', 'x_position', 'y_position')


class ArTagSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = ArTag
        fields = ('entity', 'ar_id')
