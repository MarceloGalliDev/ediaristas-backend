from django.urls import path
from .views import *

urlpatterns = [
    path('servicos/cadastrar', cadastrar_servico, name='cadastrar_servico'),
];