from django.db import models
from datetime import date, time
from django.utils import timezone


# Create an endpoint /register that accepts email, name, username, and password.
# Store the user details in the database and assign a unique primary key (PK) to each user.
# Ensure the email is unique; if the email already exists, return an error message.

class User(models.Model):
    email = models.EmailField(primary_key=True, null=False)
    name = models.CharField(null=False,max_length=20)
    username = models.CharField(null=False,max_length=20)
    password = models.CharField(null=False,max_length=20)

    class Meta:
        unique_together = ('email', 'username')


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
