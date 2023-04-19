from django.urls import path
from .views import diaristas_localidade_views

urlpatterns = [
  path('diaristas/localidades', diaristas_localidade_views.DiaristasLocalidades.as_view(), name='diaristas-localidades-list')
]