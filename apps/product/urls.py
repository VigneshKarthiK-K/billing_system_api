from django.urls import path
from .views import get_products, get_total_amount

urlpatterns = [
    path('get/', get_products, name='get-products'),
    path('total_amount/', get_total_amount, name='get-total-amount')
]