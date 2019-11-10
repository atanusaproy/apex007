from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductUpload.as_view(), name="product"),
    path("location/", views.Location.as_view(), name="location")
]