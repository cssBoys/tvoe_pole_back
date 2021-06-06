from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('playground.urls')),
    path('api/', include('news.urls')),
    path('api/', include('account.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('booking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
