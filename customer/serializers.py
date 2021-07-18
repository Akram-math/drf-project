
from customer.models import Address, Customer
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    is_company=serializers.BooleanField(default=False)
    related_company=serializers.IntegerField(allow_null=True)
    salary=serializers.DecimalField(decimal_places=2, max_digits=20, allow_null=True)
    phone=serializers.CharField(max_length=20)
    mobile=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=180)
    
    def create (self, validate_data):
        return Customer.objects.create(**validate_data)

class AddressSerializer(serializers.Serializer):
    customer=serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    type=serializers.CharField(max_length=50)
    street=serializers.CharField(max_length=500)
    zip=serializers.CharField(max_length=10)
    city=serializers.CharField(max_length=100)
    state=serializers.CharField(max_length=100)
    country=serializers.CharField(max_length=100)

    def create (self, validate_data):
        return Address.objects.create(**validate_data)

