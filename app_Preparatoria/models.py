from django.db import models

# ==========================================
# MODELO: PROFESOR
# ==========================================
class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=50, unique=True)
    apellido_profesor = models.CharField(max_length=50, unique=True)
    correo_profesor = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=50, default="")
    fecha_contratacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_profesor} {self.apellido_profesor}"

# ==========================================
# MODELO: CURSO
# ==========================================
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=100)
    creditos = models.PositiveIntegerField()
    horario = models.CharField(max_length=50)
    aula = models.CharField(max_length=20)
    profesor = models.ForeignKey(Profesor, related_name="cursos", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_curso} ({self.codigo})"

# ==========================================
# MODELO: ESTUDIANTE
# ==========================================
class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=50)
    apellido_estudiante = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)
    correo_estudiante = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_inscripcion = models.DateField(auto_now_add=True)
    cursos = models.ManyToManyField(Curso, related_name="estudiantes")

    def __str__(self):
        return f"{self.nombre_estudiante} {self.apellido_estudiante}"