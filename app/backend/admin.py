from django.contrib import admin
from backend import models

# Register your models here.
admin.site.register(models.Contract)
admin.site.register(models.Drone)
admin.site.register(models.DroneTeam)
admin.site.register(models.Player)
admin.site.register(models.TulipField)
admin.site.register(models.TulipPlant)