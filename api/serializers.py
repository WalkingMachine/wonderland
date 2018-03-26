from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'name', 'created', 'modified', 'x_position', 'y_position', 'z_position', 'yaw', 'pitch', 'roll', 'color', 'secondColor', 'thirdColor', 'fourthColor', 'gender')