from django.db import models
from apps.noticias.models import Noticia
from apps.usuario.models import Usuario
from django.conf import settings


class Comentario(models.Model):
    # usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=Usuario)
    Noticia = models.ForeignKey(Noticia, related_name='Comentario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    texto = models.TextField()
    approved_comment = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def str(self):
        return '%s - %s' % (self.Noticia.titulo, self.nombre)

    class Meta:
        ordering = ('-fecha',)