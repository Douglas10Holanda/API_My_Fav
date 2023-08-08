"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from pessoas.api import viewsets as pessoasviewsets
from filmes.api import viewsets as filmesviewsets
from series.api import viewsets as seriesviewsets
from animes.api import viewsets as animesviewsets
from jogos.api import viewsets as jogosviewsets
from categorias.api import viewsets as categoriasviewsets

route = routers.DefaultRouter()

route.register(r'pessoas', pessoasviewsets.PessoasViewsets, basename="Pessoas")
route.register(r'filmes', filmesviewsets.FilmesViewsets, basename="Filmes")
route.register(r'series', seriesviewsets.SeriesViewsets, basename="Series")
route.register(r'animes', animesviewsets.AnimesViewsets, basename="Animes")
route.register(r'jogos', jogosviewsets.JogosViewsets, basename="Jogos")
route.register(r'categorias', categoriasviewsets.CategoriasViewsets, basename="Categorias")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]