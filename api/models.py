from django.db import models
from unixtimestampfield.fields import UnixTimeStampField


# Description of an object in the arena
class Entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='unknown')

    # Type of entity (object, person, ...)
    type = models.CharField(max_length=30)

    # Id for data collector linking
    trackingId = models.IntegerField(null=True, blank=True)

    # Detected type by Yolo if it is an object.
    subType = models.CharField(max_length=60, null=True, blank=True)

    # Last time we saw the
    created = UnixTimeStampField(auto_now_add=True, use_numeric=True)
    modified = UnixTimeStampField(auto_now=True, use_numeric=True)

    # The entity is mobile or not
    mobile = models.BooleanField(default=True, blank=True)

    # Position of the entity in area
    x_position = models.FloatField()
    y_position = models.FloatField()
    z_position = models.FloatField(null=True, blank=True)

    # Euler angles of the entity
    yaw = models.FloatField(null=True, blank=True)
    pitch = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)

    # Colors of the entity
    color = models.CharField(max_length=30, null=True, blank=True)
    secondColor = models.CharField(max_length=30, null=True, blank=True)
    thirdColor = models.CharField(max_length=30, null=True, blank=True)
    fourthColor = models.CharField(max_length=30, null=True, blank=True)

    # Gender of the entity (if it is a person)
    gender = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


# Description of a area in the arena (like a room)
class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    # Left
    x_left = models.FloatField()

    # Right
    x_right = models.FloatField()

    # Up
    y_top = models.FloatField()

    # Down
    y_bottom = models.FloatField()

    def __str__(self):
        return self.name


class Waypoint(models.Model):
    waypoint_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    # Position of the waypoint
    x_position = models.FloatField()
    y_position = models.FloatField()
    yaw = models.FloatField(null=True, blank=True)

    # Many to Many links
    entities = models.ManyToManyField(Entity, blank=True)
    areas = models.ManyToManyField(Area, blank=True)

    def __str__(self):
        return self.name
