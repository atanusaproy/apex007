from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Dash.as_view(), name="dashboard"),
    path('index', views.Manage.as_view(), name="index"),
    path('eproduct', views.EditProduct.as_view(), name="eproduct"),

]