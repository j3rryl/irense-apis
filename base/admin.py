from django.contrib import admin

# Register your models here.
from .models import Room, Patient, Test

admin.site.register(Room)
admin.site.register(Patient)
admin.site.register(Test)