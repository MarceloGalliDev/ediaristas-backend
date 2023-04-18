## 1 - Criando e ativando virtualvenv
>python3 -m venv venv
>source venv/bin/activate
  - cuidado com o PATH dos pacotes, pode haver erro

## 2 - Instalando pacotes
> pip freeze
  - para verificar os pacotes instalados
> python3 -m pip install --upgrade pip setuptools wheel
  - para atualizar a wheel do sistema
> pip install Django
  - tem que ser em maiúsculo o Django, pegando a última versão
> pip install pytz
  - por alguma razão não está vindo mais com o Django a instalação do pytz
> pip install mysqlclient    
  - tem que atualizar o setuptools e wheel do bash antes
> pip install pymysql
  - incluir no arquivo settings.py
    - import pymysql
    - pymysql.install_as_MySQLdb()

## 3 - Criando projeto Django
> django-admin startproject {nome}
> cd {nome}
> python manage.py startapp {nome da app}
> pip install pymysql
  - incluir no arquivo settings.py
    - import pymysql
    - pymysql.install_as_MySQLdb()
> pip install python-decouple
  - para manusear variáveis de ambiente
> pip install unipath 
  - para gerenciar o path
> pip install cryptography
  - para adicionar a criptografia

## 4 - Conectando banco de dados
> mysql -u root -p
  - antes, verificar a instalação do mysql pelo HOMEBREW
  - digitar senha
> create database ediaristas;
  - não esquecer o ';', pois da erro se não digitado
> incluir dados no arquivo settings.py
  - incluir no campo DATABASES, dados do host porta e etc
  - incluir a aplicação noi campo de INSTALLED_APPS, na primeira posição
> python manage.py migrate
  - depois de tudo realizado, vamos incluir o migrate, para versionar nossos documentos

## 5 - Variáveis de ambiente
> pip install dotenv
  - from dotenv import load_dotenv 
  - criamos o arquivo .env, com as ambientação
  - import os

## 6 - Template admin
> pip install django-adminlte-3
  - incluir no settings.py o módulo de adminlte
  - criar pasta templates e o arquivo url
    - quando chamar-mos a rota administracao/exemplo, vamos executar o método exemplo dentro de .views que vai renderizar para nós o exemplo.html
  - AdminLTE possui bootstrap
  
## 7 - Criando models
  - Models definem a estrutura dos dados armazenados
  - importante definir o tipo de dado que será armazenado
  - Models são objetos python
  - após criar todos os campos destinados a nossa api
  > python manage.py makemigrations
    - realizar a makemigrations
  > python manage.py migrate
    - para incluir na migrate

## 8 - Criando o CRUD
  - Criamos o arquivo forms.py
  - Criamos uma classe Meta, inicializando nosso módulo de Serviço la do models.py
  - Criamos uma rota
  - Inicializamos ela na url
  - Quando a rota servicos/cadastrar for chamada > 
    - vai executar a função cadastrar_servico > 
      - vai criar uma instancia vazia do nosso formulário >
        - vai enviar essa instancia para nosso template form_servico.html
  - Incluir no template a tag form com method POST, pois vamos cadastrar algo no banco de dados

## 9 - Captando os dados para verificação
  - vamos captar os dados la do views.py, pela requisição, quando clicamos no botão cadastrar que tem o type submite, ele vai enviar a requisição no formato POST
  - usamos o is_valid() para validar as caracteristicas dadas no arquivo models.py

## 10 - Editando templates 
  - Necessário que seja no mesmo formato, nome de pasta em path
  - O Django é tido em blocos onde temos a abertura do block e o fechamendo sendo endblock

## 11 - Utilizando bootstrap
  - pip install django-bootstrap4
  - adicionar no settings.py
  - substituir {{form_servico.as_p}} por {% bootstrap_form form_servico %}

## 12 - Aplicando mascára
  - vamos aplicar mascára para formatação automática de valores monetários
  - https://cdnjs.com/libraries/jquery.mask
  - vamos incluir no nosso templates base.html o script de mask
  - <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js" integrity="sha512-pHVGpX7F/27yZ0ISY+VVjyULApbDlD0/X0rgGbTqCE7WFW5MezNTWG/dnhtbBuICzsd0WQPgpE4REBLv+UqChw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  - é necessário que seja inicializado a function()
  - fazer o replace do '.' por ','

## 13 - Criando o modelo de login
 - estamos criando o local de criar usuário para posteriormente fazer a autenticação
 - utilizamos bootstrap
 - refazemos os inputs de password para colocar lado a lado
 - criamos a rota alterar senha
 - criamos o icone de alterar senha

## 14 - Criando icones de header
 - Usamos o super para indicar que queremos o child do block

## 15 - Criando o template reset_password


## 16 - Instalando pacote Django Rest Framework
  - pip install djangorestframework
  - adicionar no settings.py a config
  - python manage.py startapp api

# 17 - Criando a tabela da API
  - incluir na settings.py a config de authentication
  - fazer a makemigration
  - quando fizer a migrate, vai dar um erro, pois ja existe uma migração inicial
  - é necessário apagar a table django_migrations na mo MySQL
  - necessario fazer uma migrate --fake
  - agora fazemos a migrate