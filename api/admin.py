from django.contrib import admin
from api.models import Entity, Object, Human, Room

# Register your models here.
admin.site.register(Object)
admin.site.register(Human)
admin.site.register(Room)
