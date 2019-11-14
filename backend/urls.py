from django.urls import path
from . import views

urlpatterns = [
    path('',views.Manage.as_view(), name="manage_index.html")
]