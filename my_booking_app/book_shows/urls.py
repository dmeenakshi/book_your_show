from django.urls import path
from .views import registration, login

urlpatterns = [
    path('registration/create_user', registration.as_view(), name="register - user"),
    path('login', login.as_view(), name="login - user")
]
