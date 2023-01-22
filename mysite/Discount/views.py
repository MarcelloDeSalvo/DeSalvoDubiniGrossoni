from django.shortcuts import render
from rest_framework.response import Response

from Discount.models import Discount
from .serializers import DiscountSerializer, CreateDiscountSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
# Create your views here.
@authentication_classes([])
@permission_classes([])
class DiscountAPIView(generics.RetrieveAPIView):
    serializer_class = DiscountSerializer

    def get_object(self):
        return self.request.user


@authentication_classes([])
@permission_classes([])
class RegisterDiscountAPIView(generics.CreateAPIView):
    serializer_class = CreateDiscountSerializer

    # Return success message after successful discount add
    def post(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        discount = serializer.save()
        return Response({
            "discount": DiscountSerializer(discount, context=self.get_serializer_context()).data,
            "message": "Discount Registered Successfully.",
        })


# Return all discounts
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getDiscounts(request):
    discounts = Discount.objects.all()
    serializer = DiscountSerializer(discounts, many=True)
    return Response(serializer.data)
    