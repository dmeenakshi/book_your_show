from django.urls import path
from .views import Registration, Login, CreateEvents, BookShow

urlpatterns = [
    path('registration/create_user', Registration.as_view(), name="register - user"),
    path('login', Login.as_view(), name="login - user"),
    path('create_event', CreateEvents.as_view(), name="create - events"),
    path('book_show', BookShow.as_view(), name='book tickets')
]
