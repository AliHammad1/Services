from django.urls import path

from apps.services.api.services import DeviceListCreateAPIView, DeviceRetrieveUpdateDestroyAPIView, HardwareIDListCreateAPIView, HardwareIDRetrieveUpdateDestroyAPIView, NetworkIDListCreateAPIView, NetworkIDRetrieveUpdateDestroyAPIView, ServiceListCreateAPIView, ServiceRetrieveUpdateDestroyAPIView, UserGroupListCreateAPIView, UserGroupRetrieveUpdateDestroyAPIView


urlpatterns = [
    # URLs for UserGroup
    path('usergroups/', UserGroupListCreateAPIView.as_view(), name='usergroup-list-create'),
    path('usergroups/<int:pk>/', UserGroupRetrieveUpdateDestroyAPIView.as_view(), name='usergroup-retrieve-update-destroy'),
    
    # URLs for Service
    path('services/', ServiceListCreateAPIView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-retrieve-update-destroy'),
    
    # URLs for Device
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyAPIView.as_view(), name='device-retrieve-update-destroy'),
    
    # URLs for HardwareID
    path('hardwareids/', HardwareIDListCreateAPIView.as_view(), name='hardwareid-list-create'),
    path('hardwareids/<int:pk>/', HardwareIDRetrieveUpdateDestroyAPIView.as_view(), name='hardwareid-retrieve-update-destroy'),
    
    # URLs for NetworkID
    path('networkids/', NetworkIDListCreateAPIView.as_view(), name='networkid-list-create'),
    path('networkids/<int:pk>/', NetworkIDRetrieveUpdateDestroyAPIView.as_view(), name='networkid-retrieve-update-destroy'),
]
