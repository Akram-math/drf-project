from django.db import models
from django.db.models.deletion import CASCADE

class Customer(models.Model):
    name=models.CharField(max_length=180)
    is_company=models.BooleanField(default=False)
    related_company=models.IntegerField(null=True, blank=True)
    salary=models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    phone=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=180)

class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=CASCADE)
    type= models.CharField(max_length=50)
    street=models.TextField()
    zip=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

