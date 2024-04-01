from rest_framework import generics

from apps.services.models import Device, HardwareID, NetworkID, Service, UserGroup
from apps.services.serializers import DeviceSerializer, HardwareIDSerializer, NetworkIDSerializer, ServiceSerializer, UserGroupSerializer


class UserGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class UserGroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer

class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DeviceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class HardwareIDListCreateAPIView(generics.ListCreateAPIView):
    queryset = HardwareID.objects.all()
    serializer_class = HardwareIDSerializer

class HardwareIDRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HardwareID.objects.all()
    serializer_class = HardwareIDSerializer

class NetworkIDListCreateAPIView(generics.ListCreateAPIView):
    queryset = NetworkID.objects.all()
    serializer_class = NetworkIDSerializer

class NetworkIDRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetworkID.objects.all()
    serializer_class = NetworkIDSerializer
