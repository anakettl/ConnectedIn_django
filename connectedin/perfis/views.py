from django.shortcuts import render
from perfis.models import Perfil
#from django.http import HttpResponse

def index(request):
	return render(request, 'index.html', {"perfis":Perfil.objects.all()})
	#return HttpResponse('Bem vindo ao Connectedin')#

def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	return render(request, 'perfil.html', {"perfil":perfil})

def convidar(request, perfil_id):
	pass

	



	# if perfil_id == '1':
	# 	perfil = Perfil('Flavio Silva', 'flavio@flavio.com.br', '76456456', 'Alura')
	# if perfil_id == '2':
	# 	perfil = Perfil('Maria Silva', 'maria@maria.com.br', '92380123', 'Net')



#disponibilizando para a funcao render o objeto perfil com seus parametros#