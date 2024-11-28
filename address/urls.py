from django.urls import path
from .views import AddressListCreateAPIView, AddressRetriveUpdateDestroyaAPIView

urlpatterns = [

    path('addresses/', AddressListCreateAPIView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetriveUpdateDestroyaAPIView.as_view(), name='address-retrive-update-destroy'),
]