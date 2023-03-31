from rest_framework import viewsets
from .models import Drone, DroneTeam, Contract, TulipField, TulipPlant, Player
from backend.serializers import (
    DroneSerializer, DroneTeamSerializer, ContractSerializer,
    TulipFieldSerializer, TulipPlantSerializer, PlayerSerializer,
)

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

class DroneTeamViewSet(viewsets.ModelViewSet):
    queryset = DroneTeam.objects.all()
    serializer_class = DroneTeamSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class TulipFieldViewSet(viewsets.ModelViewSet):
    queryset = TulipField.objects.all()
    serializer_class = TulipFieldSerializer

class TulipPlantViewSet(viewsets.ModelViewSet):
    queryset = TulipPlant.objects.all()
    serializer_class = TulipPlantSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
