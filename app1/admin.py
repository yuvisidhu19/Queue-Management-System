from django.contrib import admin
from django.db.models import fields
from .models import userData, num_counters, Employee

# Register your models here.

admin.site.register(userData)
admin.site.register(Employee)