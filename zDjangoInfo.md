# Django conection
> Execute a seguinte consulta no MYSQL Workbench
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
flush privileges;
```

> Onde root é seu usuário, localhost sua URL e password sua senha
> Em seguida, execute esta consulta para atualizar os privilégios:
> Tente se conectar usando o nó depois de fazer isso.
> Se isso não funcionar, tente sem @'localhost'parte.

# Django information
- Django possui módulo admin, por isso não podemos criar um api com nome de admin
- Django possui módulos para versionamento do banco de dados, baseado em ORM, tendo migrations já incluídas
- Django possui módulos de middlewares , para controle de segurança

## Evitando sobscrever blocks
- Para evitar a sobscrição de blocos utilizamos  {{ block.super }}

## Comandos DJANGO
- python manage.py runserver - rodar aplicação
- python mananage.py makemigrations - gerando estruturas
- python manage.py migrate - executando migrações
- python manage.py flush - limpar banco de dados
- python manage.py inspectdb > nome_da_app.models.py - mapeando outro banco de dados existente

## Validações
- As validações no DJANGO seguem um padrão:
  def validate_password(self, password):
    password_confirmation = self.initial_data['password_confirmation']
    if password != password_confirmation:
      raise serializers.ValidationError('Senhas não combinam!')
  
  - usamos sempre validate_(seguido do nome do campo)

## Desenvolvimento
1. Criamos o models.py
  - Aqui criamos as tabelas, com seus modelos e campos destinados
  - Depois de criado o models
    - python manage.py makemigrations
    - python manage.py migrate

