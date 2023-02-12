# ediaristas-backend

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

## 4 - Conectando banco de dados
> mysql -u root -p
  - antes, verificar a instalação do mysql pelo HOMEBREW
  - digitar senha
> create database ediaristas;
  - não esquecer o ';', pois da erro se não digitado
> incluir dados no arquivo settings.py
  - incluir no campo DATABASES, dados do host porta e etc
  - incluir a aplicação noi campo de INSTALLED_APPS, na primeira posição
