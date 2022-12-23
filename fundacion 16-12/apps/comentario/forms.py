from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['texto'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Comentario
        fields = ['texto']
        exclude = ['noticia']