from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User


class registration(APIView):
    def verify_if_user_exists(self, email):
        # check if user is already present
        users_details = User.objects.values_list('email', flat=True)
        if email in list(users_details):
            raise Exception("You are a registered user,Please login!")

    def post(self, request):
        email = request.GET.get('email')
        name = request.GET.get('name')
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            self.verify_if_user_exists(email)
            user_obj = User(email=email, name=name, username=username, password=password)
            user_obj.save()
            return Response(data="User is registered successfully!", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
