from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('audio.urls')),
    path('admin/', admin.site.urls),
]
