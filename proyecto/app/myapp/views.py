from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the lost dog index.")

def lista_perdidos(request):
    animals = animal.object.all().filter(perdido = True)
    context = {
        'animals': animals
    }
    return render(request, 'animals/list.html', context)

def lista_adoptar(request):
    animals = animal.object.all().filter(perdido = False)
    context = {
        'animals': animals
    }
    return render(request, 'animals/list2.html', context)
