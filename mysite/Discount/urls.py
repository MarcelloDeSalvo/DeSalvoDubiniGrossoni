from django.urls import path
from Discount.views import RegisterDiscountAPIView, getDiscounts

urlpatterns = [
  path("api/registerDiscount/",RegisterDiscountAPIView.as_view()),
  path("api/discounts/",getDiscounts),
]