from django.urls import path
from .views import registration

urlpatterns = [
    path('registration/create_user', registration.as_view(), name="register - user")
]