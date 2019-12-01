# from django.urls import path , include
# from . import  views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.HomePage.as_view(), name='home'),
# ]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login', views.Login.as_view(), name="login"),
    path('registration', views.Regis.as_view(), name="registration"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('fblogin', views.FBLogin.as_view(), name="fblogin"),
]