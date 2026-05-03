from django.urls import path
from .views import create_bill, show_bill, list_bills

urlpatterns = [
    path('create/', create_bill, name='create-bill'),
    path('show/<int:bill_id>/', show_bill, name='show-bill'),
    path('list/', list_bills, name='list-bills')
]