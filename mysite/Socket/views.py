from django.shortcuts import render
from rest_framework.response import Response
from .serializers import SocketSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

@authentication_classes([])
@permission_classes([])
class RegisterSocketAPIView(generics.CreateAPIView):
    serializer_class = SocketSerializer

    # Return success message after successful registration
    def post(self, request, *args, **kwargs):
        # Add user to request data object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        socket = serializer.save()
        return Response({
            "socket": SocketSerializer(socket, context=self.get_serializer_context()).data,
            "message": "Socket Registered Successfully.",
        })

