from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from django.urls import reverse

# 14. Funciones solicitadas para el CRUD de Profesor

def inicio_profesor(request):
    """Muestra la lista de todos los profesores."""
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return render(request, 'profesor/ver_profesor.html', context)

def agregar_profesor(request):
    """Gestiona la adición de un nuevo profesor."""
    if request.method == 'POST':
        # No hay validación de datos (Punto 30)
        nombre = request.POST.get('nombre_profesor')
        apellido = request.POST.get('apellido_profesor')
        correo = request.POST.get('correo_profesor')
        telefono = request.POST.get('telefono')
        especialidad = request.POST.get('especialidad')
        # La fecha de contratación se añade automáticamente
        
        # Crear y guardar el objeto Profesor
        Profesor.objects.create(
            nombre_profesor=nombre,
            apellido_profesor=apellido,
            correo_profesor=correo,
            telefono=telefono,
            especialidad=especialidad
        )
        return redirect('ver_profesor') # Redirige a la lista después de guardar

    return render(request, 'profesor/agregar_profesor.html')

def actualizar_profesor(request, profesor_id):
    """Muestra el formulario para editar un profesor."""
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    context = {'profesor': profesor}
    return render(request, 'profesor/actualizar_profesor.html', context)

def realizar_actualizacion_profesor(request, profesor_id):
    """Procesa el formulario de actualización de un profesor."""
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    if request.method == 'POST':
        # No hay validación de datos (Punto 30)
        profesor.nombre_profesor = request.POST.get('nombre_profesor')
        profesor.apellido_profesor = request.POST.get('apellido_profesor')
        profesor.correo_profesor = request.POST.get('correo_profesor')
        profesor.telefono = request.POST.get('telefono')
        profesor.especialidad = request.POST.get('especialidad')
        # El campo 'activo' se maneja con un checkbox
        profesor.activo = request.POST.get('activo') == 'on'
        
        profesor.save()
        return redirect('ver_profesor')

    # Si por alguna razón no es POST, redirige al formulario de actualización
    return redirect('actualizar_profesor', profesor_id=profesor_id)


def borrar_profesor(request, profesor_id):
    """Gestiona la eliminación de un profesor."""
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('ver_profesor')
        
    # El archivo borrar_profesor.html debe ser una página de confirmación
    context = {'profesor': profesor}
    return render(request, 'profesor/borrar_profesor.html', context)

def inicio_sistema(request):
    """Vista para la página de inicio general del sistema."""
    return render(request, 'inicio.html')

# ... (otras funciones existentes)

def ver_detalle_profesor(request, profesor_id):
    """Muestra los detalles de un profesor específico."""
    profesor = get_object_or_404(Profesor, pk=profesor_id)
    context = {'profesor': profesor}
    # Renderizar un nuevo HTML para el detalle
    return render(request, 'profesor/detalle_profesor.html', context)