from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Usuario

def usuario_cadastrado(sender, instance, created, **kwargs):
  if created:
    assunto = 'Cadastro realizado com sucesso!'
    corpo_email = ''
    email_destino = [instance.email, ]#instanciamos o email do usuario, vindo do models
    email_remetente = 'marcelolemesgalli@hotmail.com'
    mensagem_html = render_to_string('email_cadastro.html', {'usuario': instance})
    send_mail(assunto, corpo_email, email_remetente, email_destino, mensagem_html)
  
post_save.connect(usuario_cadastrado, sender=Usuario)

#podemos usar vários modelos de signals, podendo ser apos um delete, ou apos uma inclusão de cadastro