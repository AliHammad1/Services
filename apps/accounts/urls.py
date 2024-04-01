from django.urls import path

from apps.accounts.api.user import CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView, PartnerListCreateAPIView, PartnerRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('partners/', PartnerListCreateAPIView.as_view(), name='partner-list-create'),
    path('partners/<int:pk>/', PartnerRetrieveUpdateDestroyAPIView.as_view(), name='partner-retrieve-update-destroy'),
]
