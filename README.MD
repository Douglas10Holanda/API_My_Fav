# Descrição do Projeto
    - Criar uma aplicação que consiga mostrar os gostos favoritos de uma pessoa para séries, filmes, jogos e animes.

    - Pessoas
        Salvar, listar, deletar e Editar
    - Séries
        Salvar, listar, deletar e Editar
    - Filmes
        Salvar, listar, deletar e Editar    
    - Animes
        Salvar, listar, deletar e Editar
    - Jogos
        Salvar, listar, deletar e Editar
    - Categoria
        Salvar, listar, deletar e Editar
    - Series_fav
        Listar
    - Jogos_fav
        Listar
    - Animes_fav
        Listar
    - Filmes_fav
        Listar
    - Favoritos
        Listar

# Criação do Projeto

## Criar um ambiente virtual para cada cliente
    python -m venv my_fav1

## Ativar venv
    cd my_fav1
    cd Scripts
    activate
    cd ..
    cd ..

## Instalar Django Rest Framework
    pip install django djangorestframework

## Criar projeto django
    django-admin startproject library .

## Instalando o app para cadastro de livros
    django-admin startapp books

## Criar as tabelas do banco de dados
    python manage.py migrate

## Criar um super usuário
    python manage.py createsuperuser


## Cadastrar os apps em settings.py e sinalizar que estamos utilizando o rest framework
    'rest_framework',
    'books'

## Criamos os models de books
    from django.db import models
    from uuid import uuid4

    class Books(models.Model):
        id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255)
        release_year = models.IntegerField()
        state = models.CharField(max_length=25)
        pages = models.IntegerField()
        publishing_company = models.CharField(max_length=255)
        create_at = models.DateField(auto_now_add=True)

## Criar uma pasta chamada api dentro da app books
    Criar arquivo serializers.py e viewsets.py

## Criando o Serializer
    from rest_framework import serializers
    from books import models

    class BooksSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Books
            fields = "__all__"

## Criando a viewsets
    from rest_framework import viewsets
    from books.api import serializers
    from books import models

    class BooksViewsets(viewsets.ModelViewSet):
        serializer_class = serializers.BooksSerializer
        queryset = models.Books.objects.all()

## Criando Rotas
    from django.contrib import admin
    from django.urls import path, include

    from rest_framework import routers
    from books.api import viewsets as booksviewsets

    route = routers.DefaultRouter()

    route.register(r'books', booksviewsets.BooksViewsets, basename="Books")

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(route.urls))
    ]

# Criar migrations do modelo
    python manage.py makemigrations

# Incluir migrations criadas no banco de dados
    python manage.py migrate

# Rodar projeto 
    python manage.py runserver
