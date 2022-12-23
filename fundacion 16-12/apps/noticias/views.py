from django.shortcuts import render
from apps.comentario.models import Comentario
from apps.comentario.forms import  ComentarioForm
from django.views.generic import DeleteView, ListView, DetailView
from apps.usuario.models import Usuario
from django.urls import reverse_lazy
from apps.noticias.models import Noticia


# Create your views here.

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'noticia/listadoNoticias.html'

def registro(request):
    return render(request, 'registro/registro.html')

def Comentar(request):
    comentario = Comentari.objects.all()
    usuario = request.user.id

    context={
        'comentario' : comentario,
        'usuario': usuario,
    }
    return render(request,'comentario/listadoComentario.html', context)


def agregarComentario(request):
    usuario = Usuario(usuario = request.user)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ComentarioForm()


    context={
        'form': form,
        'usuario': usuario,
    }
    return render(request,'comentario/agregarComentario.html', context)


class DeleteComentario(DeleteView):
    model = Comentario
    template_name = 'comentario/eliminarComentario.html'
    success_url = reverse_lazy('apps.noticia:noticias')


class NoticiaDetalleView(DetailView):
    model = Noticia
    template_name = "noticias/detalleNoticia.html"