from django.urls import path
from Discount.views import RegisterDiscountAPIView

urlpatterns = [
  path("api/Discount/",RegisterDiscountAPIView.as_view()),
]