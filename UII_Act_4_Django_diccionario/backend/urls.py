from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('canales_youtube.urls')),  # 👈 conecta la app
]
