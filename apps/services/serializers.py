from rest_framework import serializers

from apps.services.models import Device, HardwareID, NetworkID, Service, UserGroup
class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class HardwareIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareID
        fields = '__all__'

class NetworkIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkID
        fields = '__all__'
