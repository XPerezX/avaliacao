# A empresa tinha um software para calcular a folha de ponto de TI
# A aplicação ficou tão boa que o diretor solicitou a mudança para que a mesma aplicação
# funcione para os varios setores e filiais da empresa
# Aplique o padrão composite visando calcular a folha de ponto da empresa

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


##############################################
class Principal(ABC):
	def __init__(self):

		@property
		def parent(self):
			return self._parent

		@parent.setter
		def parent(self, parent):
			self._parent = parent

		def adicionar_funcionario(self, component):
			pass

		def is_composite(self):
			return False





class Setor(Principal):

	def __init__(self):
		self.funcionarios = []

	def is_composite(self):
		return True

	def lista (self):


		for func in self.funcionarios:
			name = func.nome()

			print (name)


	def adicionar_funcionario(self, funcionario):
		self.funcionarios.append(funcionario)

	def Calcular_folha(self):
		custo = 0.0
		for funcionario in self.funcionarios:
			custo += funcionario.salario
		return custo






class Funcionario(Principal):

	def __init__(self, name, salario):
		self.name = name
		self.salario = salario



	def nome(self):
		nomess = self.name

		return  nomess


if __name__ == '__main__':


	SetorTi = Setor()

	funcionario = Funcionario("João", 1000)
	funcionario2 = Funcionario("Maria", 1400)
	SetorTi.adicionar_funcionario(funcionario)
	SetorTi.adicionar_funcionario(funcionario2)

	print(SetorTi.Calcular_folha())

	SetorAlmoxa = Setor()

	funcionario3 = Funcionario("Josivaldo",1600)
	funcionario4 = Funcionario("Edivaldo", 2000)

	SetorAlmoxa.adicionar_funcionario(funcionario3)
	SetorAlmoxa.adicionar_funcionario(funcionario4)

	print(SetorAlmoxa.Calcular_folha())