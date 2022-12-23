from django.urls import path
from .views import NoticiaListview, NoticiaDetalleView

urlpatterns = [
    path("noticias", NoticiaListview.as_view()),
    path('detalle/<int:pk>', NoticiaDetalleView.as_view(), name='detalle'),
    
]

  