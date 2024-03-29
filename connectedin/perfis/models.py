from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)

	def convidar(self, perfil_convidado):
		Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

	# Create your models here.
#def __init__: funcao construtora
#quando a model e herdada de .models nao e necessaria a funcao init

'''
class Perfil(object):
	def __init__(self, nome='', email='', telefone='', nome_empresa=''):
		self.nome = nome
		self.email = email
		self.telefone = telefone
		self.nome_empresa = nome_empresa
'''
# Create your models here.
#def __init__: funcao construtora


