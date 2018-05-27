from django.db import models


# Description of an object in the arena
class Entity(models.Model):
    entityId = models.AutoField(primary_key=True)
    entityClass = models.CharField(max_length=30)
    entityName = models.CharField(max_length=30, null=True, blank=True)
    entityCategory = models.CharField(max_length=30, null=True, blank=True)
    entityColor = models.CharField(max_length=30, null=True, blank=True)
    entityWeight = models.FloatField(default=None, null=True, blank=True)
    entitySize = models.FloatField(default=None, null=True, blank=True)

    entityIsRoom = models.BooleanField(default=False, blank=True)
    entityIsWaypoint = models.BooleanField(default=False, blank=True)
    entityIsContainer = models.BooleanField(default=False, blank=True)
    entityGotPosition = models.BooleanField(default=False, blank=True)

    # The position of the object in space if available
    entityPosX = models.FloatField(default=None, null=True, blank=True)
    entityPosY = models.FloatField(default=None, null=True, blank=True)
    entityPosZ = models.FloatField(default=None, null=True, blank=True)
    entityPosYaw = models.FloatField(default=None, null=True, blank=True)
    entityPosPitch = models.FloatField(default=None, null=True, blank=True)
    entityPosRoll = models.FloatField(default=None, null=True, blank=True)

    # The position to reach to be able to catch the object
    entityWaypointX = models.FloatField(default=None, null=True, blank=True)
    entityWaypointY = models.FloatField(default=None, null=True, blank=True)
    entityWaypointYaw = models.FloatField(default=None, null=True, blank=True)

    # Just for serializer
    depth_waypoint = models.IntegerField(null=True, blank=True)
    depth_position = models.IntegerField(null=True, blank=True)

    entityContainer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.entityClass + " - " + str(self.entityId)


# Description of an object in the arena
class People(models.Model):
    peopleId = models.AutoField(primary_key=True)
    peopleRecognitionId = models.IntegerField(null=False, blank=False, unique=True)

    peopleName = models.CharField(max_length=30, null=True, blank=True)
    peopleAge = models.IntegerField(null=True, blank=True)

    peopleColor = models.CharField(max_length=30, null=True, blank=True)

    peoplePose = models.CharField(max_length=30, null=True, blank=True)
    peoplePoseAccuracy = models.FloatField(default=None, null=True, blank=True)

    peopleEmotion = models.CharField(max_length=30, null=True, blank=True)
    peopleEmotionAccuracy = models.FloatField(default=None, null=True, blank=True)

    peopleGender = models.CharField(max_length=10, null=True, blank=True)
    peopleGenderAccuracy = models.FloatField(default=None, null=True, blank=True)

    peopleIsOperator = models.BooleanField(default=False)

    def __str__(self):
        return str(self.peopleId) + "(" + str(
            self.peopleRecognitionId) + ") - " + self.peopleGender + " - " + self.peopleColor + " - " + self.peoplePose
