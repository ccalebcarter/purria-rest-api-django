from django.urls import path, include
from rest_framework import routers
from .views import (
    DroneViewSet, DroneTeamViewSet, ContractViewSet,
    TulipFieldViewSet, TulipPlantViewSet, PlayerViewSet,
)

router = routers.DefaultRouter()

router.register(r'drones', DroneViewSet)
router.register(r'drone-teams', DroneTeamViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'tulip-fields', TulipFieldViewSet)
router.register(r'tulip-plants', TulipPlantViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]