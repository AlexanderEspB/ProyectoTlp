from django.db import models
from django.contrib.auth.models import User

class Segmento(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TIPO_CHOICES = [
        ('COMUNIDAD USM',"Comunidad USM"),
        ('ESTUDIANTE',"Estudiante"),
        ('PROFESOR',"Profesor"),
        ('JEFE DE CARRERA',"Jefe de Carrera"), 

    ]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    def str(self):
        return f"{self.user} {self.tipo}"
class Evento(models.Model):
    TIPO_CHOICES = [
        ('VACACIONES', 'Vacaciones'),
        ('FERIADO', 'Feriado'),
        ('SUSPENSION DE ACTIVIDADES', 'Suspensión de Actividades'),
        ('SUSPENSION DE ACTIVIDADES (PM)', 'Suspensión de Actividades (PM)'),
        ('CEREMONIA', 'Ceremonia'),
        ('EDDA', 'Edda'),
        ('EVALUACION', 'Evaluacion'),
        ('AYUDANTIAS', 'Ayudantias'),
        ('HITO ACADEMICO', 'Hito Academicas'),
        ('SECRETARIA ACADEMICA', 'Secretaria Academica'),
        ('OAI', 'Oai'),
    ]

    fecha_inicio=models.DateTimeField()
    fecha_termino=models.DateTimeField()
    titulo=models.CharField(max_length=120)
    descripcion=models.CharField(max_length=600)
    tipo=models.CharField(max_length=50, choices=TIPO_CHOICES)
    segmento=models.ForeignKey(Segmento, on_delete=models.CASCADE)
