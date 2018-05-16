from rest_framework import serializers

from models import Entity, People


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('entityId', 'entityClass', 'entityName', 'entityCategory','entityColor', 'entityWeight', 'entitySize','entityContainer',
                  'entityPosX', 'entityPosY', 'entityPosZ', 'entityPosYaw', 'entityPosPitch', 'entityPosRoll',
                  'entityWaypointX', 'entityWaypointY', 'entityWaypointYaw',
                  'depth_waypoint', 'depth_position'
                  )


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('peopleId', 'peopleRecognitionId', 'peopleColor', 'peopleName',
                  'peoplePose', 'peoplePoseAccuracy',
                  'peopleGender', 'peopleGenderAccuracy', 'peopleIsOperator'
                  )
