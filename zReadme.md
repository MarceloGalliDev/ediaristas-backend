**kwargs = argumentos

# - Composição da estrutura
  - services, para logicas de negocios
  - serializers, para enviar somente os dados necessarios
  - views, para tratar das requisições

# - Fluxo de criação
  - models = onde criamos as tabelas no banco de dados
    - makemigrations e migrate
  - serializers = tratamento dos dados e onde colocamos a disposição ao end-point os campos que desejamos
  - views = onde recebemos os dados do front-end e as requisições
  - url = onde a view seja executada


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
  - se acaso não funcionar, tem que deletar o DB e fazer migrate novamente

# 18 - Criando a API de busca por cep
  - vamos utilizar o serializer, que significa transformar a resposta de um objeto em json
  - serializer é usado para definir o formato de uma resposta atraves de uma requisição
  - criaremos uma nova pasta para receber as views
  - criaremos uma classe
  - criaremos a url patterns
  - o many=True, dentro do serializer é para indicar que estamos fazendo uma ligação n to n
  - fazemos o teste no imsonia

# 19 - Criando services
  - agora criaremos uma pasta services, para armazenar nossas requisições externas

# 20 - Buscar CEP pelo IBGE
  - criamos a pasta services
  - criamos uma classe para paginar a quantidade de diaristas disponibilizado na consulta
  - incluimos na requisição e serializamos

# 21 - Liberando API via CORS
  - https://pypi.org/project/django-cors-headers/
  - pip install django-cors-headers
  - controle de disponibilização de API, para mobile e web
  - bloqueia requisições anonimas, e authentication com segurança
  - fazer as config conforme a documentação

# 22 - Criando novo end-point
  - buscando cep incluindo path para busca(end point)

# 23 - Serializando o end-point
  - serializamos o end-point, para reorganizando o data
  - utilizamos um base serializer

# 24 - Validando os dados de cadastro e pesquisa
  - vamos utilizar o buscar_cidade_cep(cep), reaproveitando a função

# 25 - Listagem de serviço
  - criamos os arquivos de servico_view puxando para API os dados de servico vindo da administração
  - e serializamos os dados

# 26 - Criando services na administração
  - estamos criando a pasta para logica de negocio dentro da administração

# 27 - HATEOAS
  - visa facilitar os end-points da nossa aplicação
  - facilitar a navegação entre os links da nossa navegação

# 28 - Serializamos o cadastro
  - iniciamos o end-point de cadastro
  - realizamos as validações
  - criamos o managers 
    - obrigatório ter get_queryset()

# 29 - Authentication
  - simpleJWT
  - pip install djangorestframework-simplejwt
  - segue a documentação
  - adicionar no settings.py
  - verificar o method padrão no arquivo de models
    - refresh token - token para atualizar o access token, 
      - necessário incluir o path
    - access token - token de acesso, possui tempo de expiração
      - necessário incluir o path

# 30 - Criação do me_view()
  - dados dos usuarios logados
  - request.user me retorna os dados do usuario logado
  - necessario privar a rota, para somente quando estiver logado ter o acesso

# 31 - Criando conta no mailgun
  - incluir os dados no settings.py
  - verificar a api e password na página do mailgun

# 32 - Criando signals.py
  - métodos que vão realizar alguma coisa
  - o django possui vários sinais que poder nos ajudar a realizar alguma solução, isso quando atualizado nosso banco

# 33 - Criando arquivos de enviroment
  - pip install django-environ

# 34 - Cadastro de diárias
  - on_delete=DO_NOTHING - esse campo significa que ao deletar não iremos fazer nada
  - related_name='cliente' - esse campo serve para nos termos acesso ao cliente da diária solicitada.
  - quando temos umas relação N para N, usamos o ManyToManyField()
  - auto_now_add=True - esse campo pega a data e hora do servidor quando for chamada o método
  - adicionar o makemigration e migrate
  - vamos capturar o access token e o servico

# 35 - Listando comissão de serviçoes
  - temos que receber esse dado apartir do service da pasta administração