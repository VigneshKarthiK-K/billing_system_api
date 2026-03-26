# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import store_bill_details

# Create your views here.
@api_view(['POST'])
def create_bill(request):
    bill_data = request.data

    bill = store_bill_details(bill_data)
    return Response({'message': f'Bill {bill.id} created successfully'})
