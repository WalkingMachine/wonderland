from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Area


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('entity_id', 'name', 'created', 'modified', 'x_position',
                  'y_position', 'z_position', 'yaw', 'pitch', 'roll',
                  'color', 'secondColor', 'thirdColor', 'fourthColor',
                  'gender')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('area_id', 'name', 'x_left', 'x_right', 'y_top', 'y_bottom')
