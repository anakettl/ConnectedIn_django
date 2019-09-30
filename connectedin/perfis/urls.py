from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar')
)

#a rowstring ignora todos os scapes codes, a string normal nao, o ^ indica que estamos procurando a palavra no incio da string e o dolar no final#
#na expressao regular para colocar na rota um numero (id) adicionamos \d, + mais indica q pode ter um ou mais digitos#
#(?P<perfil_id>\d+)$ extrai para o grupo perfil_id#