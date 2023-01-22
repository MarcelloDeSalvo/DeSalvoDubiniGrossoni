from django.urls import path
from Discount.views import RegisterDiscountAPIView, getDiscounts, RemoveDiscountAPIView

urlpatterns = [
  path("api/registerDiscount/",RegisterDiscountAPIView.as_view()),
  path("api/removeDiscount/",RemoveDiscountAPIView.as_view()),
  path("api/discounts/",getDiscounts),
]