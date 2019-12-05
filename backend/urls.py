from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dash.as_view(), name="dashboard"),
    path('index', views.Manage.as_view(), name="index"),
]