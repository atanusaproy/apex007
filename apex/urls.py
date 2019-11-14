
from django.contrib import admin
from django.urls import path, include
from apex_app import urls as app_urls
from product import urls as pro_urls
from backend import urls as backend_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_urls)),
    path('product/', include(pro_urls)),
    path('backend/', include(backend_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
