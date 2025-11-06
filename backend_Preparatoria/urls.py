from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Enlace a las URLs de la aplicación (Punto 26)
    path('', include('app_Preparatoria.urls')), 
]