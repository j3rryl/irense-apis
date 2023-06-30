from rest_framework.serializers import ModelSerializer
from .models import Room, Patient

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'