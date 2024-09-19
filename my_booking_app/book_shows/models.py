from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from datetime import date, time
from django.utils import timezone


# Create an endpoint /register that accepts email, name, username, and password.
# Store the user details in the database and assign a unique primary key (PK) to each user.
# Ensure the email is unique; if the email already exists, return an error message.

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=30, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # passsword field comes from abstract user
    # password = models.CharField(null=False, max_length=20)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

# class Events(models.Model):
#     LOCATION = {
#         "BLR": "Bangalore",
#         "HYD": "Hyderabad",
#         "PUNE": "Pune",
#         "CHEN": "Chennai"
#     }
#     title = models.CharField(null=False)
#     description = models.CharField(null=False)
#     event_created_on = models.DateField(default=date.today)
#     event_created_at = models.TimeField(default=timezone.now().time())
#     location = models.CharField(max_length=4, choices=LOCATION)
#     tickets = models.IntegerField(null=False)
#
#
# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
