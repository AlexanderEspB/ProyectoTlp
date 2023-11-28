from django.shortcuts import render
from .models import Evento
from django.http import HttpResponse

def index(request):
    eventos = Evento.objects.all()
    return render(request,'miapp/index.html', {'eventos': eventos})
def index2(request):
    eventos = Evento.objects.all()
    return render(request,'miapp/index2.html', {'eventos': eventos})

