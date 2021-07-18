from django.db import models
class Member(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    addres = models.TextField(blank=True)
# Create your models here.
