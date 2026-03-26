from django.urls import path
from .views import create_bill

urlpatterns = [
    path('create/', create_bill, name='create-bill')
]