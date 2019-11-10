from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductDetails.as_view(), name="productup.html")
]