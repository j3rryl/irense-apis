from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class Patient(models.Model):
    first_name=models.TextField(null=False)
    last_name=models.TextField(null=False)
    email=models.EmailField(null=True, blank=True)
    phone_number=models.TextField(null=False)
    age=models.IntegerField(null=False)
    gender=models.TextField(null=False)
    last_test_date=models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name+" "+self.last_name


class User(models.Model):
    first_name=models.TextField(null=False)
    last_name=models.TextField(null=False)
    email=models.EmailField(null=True, blank=True)
    phone_number=models.TextField(null=False)
    age=models.IntegerField(null=False)
    gender=models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Test(models.Model):
    first_name=models.TextField(null=False)
    last_name=models.TextField(null=False)
    email=models.EmailField(null=True, blank=True)
    phone_number=models.TextField(null=False)
    age=models.IntegerField(null=False)
    gender=models.TextField(null=False)
    test_date=models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


