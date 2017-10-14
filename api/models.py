from django.db import models
from datetime import date


class Entity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    time = models.DateTimeField(null=True)
    x_position = models.FloatField(null=True)
    y_position = models.FloatField(null=True)
    z_position = models.FloatField(null=True)

    def __str__(self):
        return "{}".format(self.name)


class Human(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, null=True)
    gender = models.CharField(max_length=1, null=True)
    person_name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return "{}".format(self.person_name)


class Object(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, null=True)
    type = models.CharField(max_length=20, null=True)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{}".format(self.type)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, null=True)

    x1 = models.FloatField()
    x2 = models.FloatField()
    x3 = models.FloatField()
    x4 = models.FloatField()

    y1 = models.FloatField()
    y2 = models.FloatField()
    y3 = models.FloatField()
    y4 = models.FloatField()

    room_name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.room_name)


class Waypoint(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, null=True)
    x_position = models.FloatField()
    y_position = models.FloatField()

    def __str__(self):
        return "{}".format(self.entity.name)


class ArTag(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entity, null=True)
    ar_id = models.IntegerField(null=True)

    def __str__(self):
        return "{}".format(self.entity.name)
