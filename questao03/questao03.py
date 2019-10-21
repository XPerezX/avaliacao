# A empresa tinha um software para calcular a folha de ponto de TI
# A aplicação ficou tão boa que o diretor solicitou a mudança para que a mesma aplicação
# funcione para os varios setores e filiais da empresa
# Aplique o padrão composite visando calcular a folha de ponto da empresa

class Funcionario:
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

class SetorTi:

	def __init__(self):
		self.funcionarios = []

	def adiciona_usuario(self, funcionario):
		self.funcionarios.append(funcionario)

	def calcula_folha(self):
		custo = 0.0
		for funcionario in self.funcionarios:
			custo += funcionario.salario
		return custo 

class Principal:
	def __init__(self):
		funcionario = Funcionario("joao", 1000)
		funcionario2 = Funcionario("maria", 1400)

		setor = SetorTi()
		setor.adiciona_usuario(funcionario)
		setor.adiciona_usuario(funcionario2)

		print("O custo da Folha de TI é " + str(setor.calcula_folha()))


if __name__ == '__main__':
	principal = Principal()