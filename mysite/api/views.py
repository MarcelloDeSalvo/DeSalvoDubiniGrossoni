from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer, LoginSerializer
from User.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import permissions
from rest_framework import views
from rest_framework.request import Request
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication
from User.authentication import EmailAuthBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

@authentication_classes([EmailAuthBackend, SessionAuthentication])
class LoginView(views.APIView):
# This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print("Received: ", request.data, " request")
        serializer = LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user, backend='User.authentication.EmailAuthBackend')
        return Response(None, status=status.HTTP_202_ACCEPTED)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


@authentication_classes([EmailAuthBackend, SessionAuthentication])
@permission_classes([IsAuthenticated])
def isLogged(request: Request) -> Response:
    return Response(UserSerializer(request.user).data)
