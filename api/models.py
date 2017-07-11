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
