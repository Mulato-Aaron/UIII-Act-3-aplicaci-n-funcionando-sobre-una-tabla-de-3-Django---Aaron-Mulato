from django.urls import path
from . import views

urlpatterns = [
    # Rutas generales
    path('', views.inicio_sistema, name='inicio_sistema'),
    
    # Rutas para el modelo PROFESOR
    path('profesor/', views.inicio_profesor, name='ver_profesor'),
    path('profesor/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesor/actualizar/<int:profesor_id>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesor/actualizar_guardar/<int:profesor_id>/', views.realizar_actualizacion_profesor, name='realizar_actualizacion_profesor'),
    path('profesor/borrar/<int:profesor_id>/', views.borrar_profesor, name='borrar_profesor'),
    path('profesor/detalle/<int:profesor_id>/', views.ver_detalle_profesor, name='ver_detalle_profesor'),
]