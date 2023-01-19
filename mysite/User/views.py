from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from User.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
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

# Create your views here.
class UserAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    # Return success message after successful registration
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Registered Successfully.  Now perform Login to get your token",
        })

        


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(('POST',))
def isLogged(request):
    if request.user.is_authenticated:
        # The user is authenticated
        print("User is authenticated", request.user)
        return Response("Authorized", status=200)
    else:
        # The user is not authenticated
        return Response("Unauthorized", status=401)