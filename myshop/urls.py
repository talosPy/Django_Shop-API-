from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myshop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),  # Updated to use 'carts/'
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
