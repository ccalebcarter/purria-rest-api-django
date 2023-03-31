from rest_framework import serializers
from .models import Drone, DroneTeam, Contract, TulipField, TulipPlant, Player

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

class DroneTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneTeam
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class TulipFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = TulipField
        fields = '__all__'

class TulipPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TulipPlant
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
