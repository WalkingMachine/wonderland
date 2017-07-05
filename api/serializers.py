from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Human, Object


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
