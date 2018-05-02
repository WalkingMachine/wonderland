from rest_framework import serializers
from api.models import Entity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('entityId', 'entityClass', 'entityName', 'entityCategory', 'entityContainer',
                  'entityPosX', 'entityPosY', 'entityPosZ', 'entityPosYaw', 'entityPosPitch', 'entityPosRoll',
                  'entityWaypointX', 'entityWaypointY', 'entityWaypointYaw',
                  'depth_waypoint', 'depth_position'
                  )
