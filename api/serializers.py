from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Human, Object


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('name', 'time')


class HumanSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Entity
        fields = ('entity')


class ObjectSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)

    class Meta:
        model = Entity
        fields = ('entity')
