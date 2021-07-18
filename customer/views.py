from requests.api import get
from customer.models import Address, Customer
from django.shortcuts import render
import requests
from django.http import JsonResponse
# from django.shortcuts import render
from rest_framework.views import APIView
from django.core.checks import messages
from rest_framework.parsers import JSONParser
from customer.serializers import CustomerSerializer,AddressSerializer

# Create your views here.
class CustomerView (APIView):

    def post(self,request):
        _url = "http://b92f40ed78c0.ngrok.io/transaction/"
        data_api = requests.get(_url).json()

        for da in data_api:
            customer_data ={
                'name' : da['name'],
                'is_company' : da['is_company'],
                'salary' : da['penghasilan'],
                'phone' : da['phone'],
                'mobile': da['mobile'],
                'email' : da['email'],
                'related_company' : da['related_company'],
            }

            address_data ={
                'type':da['address_type'],
                'street':da['street'],
                'zip':da['zip'],
                'city':da['city'],
                'state':da['state'],
                'country':da['country']
            
            }

            cstm = CustomerSerializer (data=customer_data)
            if cstm.is_valid(raise_exception=True):
                cstm.save()

                id_customer=cstm.data['id']

                address_data['customer'] = id_customer

                addr=AddressSerializer(data=address_data)

                if addr.is_valid(raise_exception=True):
                    addr.save()

                continue
            else:
                return JsonResponse(status=400, data={"messages": "Failed"},safe=False)

        return JsonResponse(status=200, data={"messages": "Succses"},safe=False) 

    def get(self, request):

        customer=Customer.objects.all()
        customer_serializer=CustomerSerializer(customer, many=True)
        res=customer_serializer.data
        
        return JsonResponse(status=200, data=res, safe=False)