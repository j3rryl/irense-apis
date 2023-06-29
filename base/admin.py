from django.contrib import admin

# Register your models here.
from .models import Room, Patient, Test, Topic, Message

admin.site.register(Room)
admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(Topic)
admin.site.register(Message)