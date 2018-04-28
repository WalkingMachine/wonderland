from django.db import models


# Description of an object in the arena
class Entity(models.Model):
    entityId = models.AutoField(primary_key=True)
    entityClass = models.CharField(max_length=30)
    entityName = models.CharField(max_length=30, null=False, blank=True)

    # Entity attributes
    entityIsRoom = models.BooleanField(default=False, null=False, blank=True)
    entityIsWaypoint = models.BooleanField(default=False, null=False, blank=True)
    entityIsContainer = models.BooleanField(default=False, null=False, blank=True)
    entityIsMobile = models.BooleanField(default=False, null=False, blank=True)

    entityContainer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.entityClass + " - " + str(self.entityId)
