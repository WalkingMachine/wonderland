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
    name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=1, null=True)
    x_position = models.FloatField(null=True)
    y_position = models.FloatField(null=True)
    z_position = models.FloatField(null=True)

    def __str__(self):
        return "{}".format(self.name)

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    type = models.CharField(max_length=20, null=True)

    x_position = models.FloatField()
    y_position = models.FloatField()
    z_position = models.FloatField(null=True)
    def __str__(self):
        return "{}".format(self.name)


class Object(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    room = models.ForeignKey(Room, models.SET_NULL, null=True, blank=True)

    x_position = models.FloatField(null=True, blank=True)
    y_position = models.FloatField(null=True, blank=True)
    z_position = models.FloatField(null=True, blank=True)
    theta = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

class Waypoint(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    x_position = models.FloatField()
    y_position = models.FloatField()

    def __str__(self):
        return "{}".format(self.name)


class ArTag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, default='')
    ar_id = models.IntegerField(null=True)
    x_position = models.FloatField(null=True)
    y_position = models.FloatField(null=True)
    z_position = models.FloatField(null=True)
    theta = models.FloatField(null=True)

    def __str__(self):
        return "{}".format(self.name)
