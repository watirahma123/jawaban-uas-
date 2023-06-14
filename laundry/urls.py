from django.contrib import admin
from django.urls import path
from pelanggan.views import pelanggan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pelanggan/', pelanggan),
]
