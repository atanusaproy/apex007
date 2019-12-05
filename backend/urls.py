from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard.as_view(), name="dashboard.html"),
    path('index', views.Manage.as_view(), name="manage_index.html")
]