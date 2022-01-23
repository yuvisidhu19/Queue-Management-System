from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField   #same as OneToOneField but data is saved automatically when a model is created

# Create your models here.

#Employee details
class Employee(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    counterNumber = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}"

#Customer details
class userData(models.Model):
    name = models.CharField(max_length = 100)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    email = models.EmailField()
    otp = models.CharField(max_length = 6)
    counter = models.IntegerField(null=True)
    pos = models.IntegerField(null=True)
    token = models.IntegerField(null=True)

    #renaming data stored in this model
    def __str__(self):
        return f"{self.name}"

#counter number assigned to employee (acts as total number of counters for admin)
class num_counters(models.Model):
    num_counters = models.IntegerField(null=True)
