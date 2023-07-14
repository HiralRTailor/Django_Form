from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class UserInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    profile_picture_path = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
