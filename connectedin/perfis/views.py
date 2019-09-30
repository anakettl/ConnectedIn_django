from django.shortcuts import render, redirect
from perfis.models import Perfil
#from django.http import HttpResponse

def index(request):
	return render(request, 'index.html', {"perfis":Perfil.objects.all()})
	#return HttpResponse('Bem vindo ao Connectedin')#

def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	return render(request, 'perfil.html', {"perfil":perfil})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')
#	return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)

	



	# if perfil_id == '1':
	# 	perfil = Perfil('Flavio Silva', 'flavio@flavio.com.br', '76456456', 'Alura')
	# if perfil_id == '2':
	# 	perfil = Perfil('Maria Silva', 'maria@maria.com.br', '92380123', 'Net')



#disponibilizando para a funcao render o objeto perfil com seus parametros#