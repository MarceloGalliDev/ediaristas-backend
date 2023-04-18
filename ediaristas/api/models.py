import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_image_file_extension
from localflavor.br.models import BRCPFField

#renomeando os arquivos de fotos
def nome_arquivo_usuario(instance, filename):
  ext = filename.split('.')[-1]
  filename = '%s.%s' % (uuid.uuid4(), ext)
  return os.path.join('usuarios', filename)

def nome_arquivo_documento(instance, filename):
  ext = filename.split('.')[-1]
  filename = '%s.%s' % (uuid.uuid4(), ext)
  return os.path.join('documentos', filename)

class Usuario(AbstractUser):
  TIPO_USUARIO_CHOICES = (
    (1, "Cliente"),
    (2, "Diaristas")
  )
  nome_completo = models.CharField(max_length=255, null=False, blank=True)
  cpf = BRCPFField(null=False, unique=True)
  nascimento = models.DateField(null=False, blank=True)
  email = models.EmailField(null=False, blank=False, unique=True)
  telefone = models.CharField(max_length=11, null=False, blank=False)
  tipo_usuario = models.IntegerField(choices=TIPO_USUARIO_CHOICES, null=False, blank=False)
  reputacao = models.FloatField(null=False, blank=False, default=5)
  chave_pix = models.CharField(null=True, blank=True, max_length=255)
  foto_usuario = models.ImageField(null=False, upload_to=nome_arquivo_usuario, validators=[validate_image_file_extension, ]) #incluimos um renomeador de nome, e um validador de imagem
  foto_documento = models.ImageField(null=False, upload_to=nome_arquivo_documento, validators=[validate_image_file_extension, ]) #incluimos um renomeador de nome, e um validador de imagem