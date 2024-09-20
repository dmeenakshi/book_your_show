from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from book_shows.models import User, Events


class Registration(APIView):
    def verify_if_user_exists(self, email):
        # check if user is already present
        users_details = User.objects.filter(email=email).exists()
        print(users_details)
        if users_details:
            raise Exception("You have already registered,Please log in!")

    def post(self, request):
        email = request.GET.get('email')
        name = request.GET.get('name')
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            self.verify_if_user_exists(email)
            # if user doesn't exist then create user in User table
            user_obj = User(email=email, name=name, username=username)
            user_obj.set_password(password)
            user_obj.save()
            return Response(data="User is registered successfully!", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    # permission_classes = (permissions.AllowAny,)
    def authenticate(self, request, email=None, password=None, **kwrgs):
        try:
            user = User.objects.get(email=request.GET.get('email'))
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def post(self, request, *args, **kwargs):
        try:
            email = request.GET.get('email')
            password = request.GET.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                })
        except Exception as e:
            return Response({'error': "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


class CreateEvents(APIView):
    # /create_event
    def post(self, request):
        title = request.GET.get('title')
        description = request.GET.get('description')
        location = request.GET.get('location')
        ticket_available = int(request.GET.get('ticket_available'))
        try:
            Events.objects.create(title=title, description=description,
                                  location=location, tickets=ticket_available)
            # event_obj.save()
            return Response({"message": "Event is created"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            Response({"error": f"Something went wrong here,{e}!"}, status=status.HTTP_400_BAD_REQUEST)


# class BookShow(APIView):
#     def post(self, request):
#         try:
#             # email id and event name
#             email_id = request.GET.get('email')
#             event_name = request.GET.get('event_name')
#             if User.objects.filter(email=email_id).exists:
#                 print(User.objects.filter(email=email_id))
#             return Response("Booking is done!")
#         except Exception as e:
#             return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
