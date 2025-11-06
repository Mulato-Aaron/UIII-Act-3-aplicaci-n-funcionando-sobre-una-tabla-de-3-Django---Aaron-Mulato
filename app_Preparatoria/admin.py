from django.contrib import admin
from .models import Profesor, Curso, Estudiante

# Registrar modelos (Punto 27)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)