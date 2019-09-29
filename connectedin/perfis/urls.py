from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index', name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir', name='exibir')
)

#a rowstring ignora todos os scapes codes, a string normal nao, o ^ indica que estamos procurando a palavra no incio da string e o dolar no final#
#na expressao regular para colocar na rota um numero (id) adicionamos \d, + mais indica q pode ter um ou mais digitos#
#(?P<perfil_id>\d+)$ extrai para o grupo perfil_id#