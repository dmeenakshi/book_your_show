from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from datetime import date, time
from django.utils import timezone


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=30, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class Events(models.Model):
    class location_choices(models.TextChoices):
        BLR = "Bangalore"
        HYD = "Hyderabad"
        PUNE = "Pune"
        CHEN = "Chennai"
    title = models.CharField(unique=True, max_length=250)
    description = models.CharField(null=False, max_length=250)
    event_created_on = models.DateField(default=date.today)
    event_created_at = models.TimeField(default=timezone.now)
    location = models.CharField(max_length=9, choices=location_choices.choices)
    tickets = models.IntegerField(null=False)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
