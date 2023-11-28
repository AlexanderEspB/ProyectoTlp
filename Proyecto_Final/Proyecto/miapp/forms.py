from django import forms
from .models import Evento

class EventoForm(forms.Form):
    TIPO_CHOICES = [
        ('', 'Todos'),  
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
    SEGMENTO_CHOICES = [
        ('', 'Todos'), 
        ('COMUNIDAD USM', 'Comunidad USM'),
        ('ESTUDIANTE', 'Estudiante'),
        ('PROFESOR', 'Profesor'),
        ('JEFE DE CARRERA', 'Jefe de Carrera'),
    ]

    tipo = forms.ChoiceField(choices=TIPO_CHOICES, required=False, widget=forms.Select(attrs={'class': 'btn btn-secondary btn-sm'}))
    segmento = forms.ChoiceField(choices=SEGMENTO_CHOICES, required=False, widget=forms.Select(attrs={'class': 'btn btn-secondary btn-sm'}))