from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from apps.noticias.models import Noticia



# def Index(request):
#     return render(request, "base.html")

def quienes_somos(request):
    return render(request, "quienes_somos.html")

def listadoNoticias(request):
    return render(request, "listadoNoticias.html")

def voluntariado(request):
    return render(request, "voluntariado.html")

def programas(request):
    return render(request, "programas.html")

# def contacto(request):
#     data = {
#         'form': ContactoForm()
#     }
#     return render(request, "contacto.html", data)

def iniciosession(request):
    return render(request, "index.html")

def noticias(request):
    return render(request, "blog.html")

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='/')
        data['form'] = formulario
    
    return render(request, "registration/registro.html", data)


def contacto(request):
    return render(request, "contacto.html")

def post(request):
    return render(request, "post.html")

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'base.html'