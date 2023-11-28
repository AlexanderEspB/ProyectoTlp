from django.shortcuts import render
from .models import Evento
from django.http import HttpResponse
from .forms import EventoForm

def index(request):
    eventos = Evento.objects.select_related('segmento').all()
    form = EventoForm(request.GET)
    if form.is_valid():
        tipo_filter = form.cleaned_data.get('tipo', '')
        segmento_filter = form.cleaned_data.get('segmento', '')
        if tipo_filter:
            eventos = eventos.filter(tipo=tipo_filter)
        if segmento_filter:
            eventos = eventos.filter(segmento__tipo=segmento_filter)

    return render(request, 'miapp/index.html', {'eventos': eventos, 'form': form})

def index2(request):
    eventos = Evento.objects.select_related('segmento').all()
    form = EventoForm(request.GET)
    if form.is_valid():
        tipo_filter = form.cleaned_data.get('tipo', '')
        segmento_filter = form.cleaned_data.get('segmento', '')
        if tipo_filter:
            eventos = eventos.filter(tipo=tipo_filter)
        if segmento_filter:
            eventos = eventos.filter(segmento__tipo=segmento_filter)

    return render(request, 'miapp/index2.html', {'eventos': eventos, 'form': form})

