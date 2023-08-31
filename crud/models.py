from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    country = CountryField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

