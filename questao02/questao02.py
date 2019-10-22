# 
# O sistema hoje possui uma classe para se conectar ao banco de dados local
# Foi feito o deploy do sistema para a aws, mas a string de conexão mudou
# Vocês tem que prover uma nova classe de conexão com o banco e utilizar 
# algum padrão de projeto para flexibilizar as conexões com o banco
# o ideal é que a classe principal não saiba em qual banco ele está conectando
# e que so haja uma instancia de cada classe de conexão ao banco

class Principal:
	__instance = None

	def __init__(self):
		self

	def build(self, tipo):
		factory = Factory()

		if tipo == "local":
			local = factory.build("local")

		elif tipo == "producao":
			local = factory.build("producao")


	def instance(self):
		if not Principal.__instance:
			Principal.__instance = Principal()
		return Principal.__instance




# classe de conexao com o banco em desenv no mysql
class Banco:

	def __init__(self):
		self.endereco = "localhost"
		self.usuario = "root"
		self.senha = "senhaforte"
		self.db = "desenv"

	def get_url_connection(self):
		return "Server="+self.endereco+";Database="+self.db+";Uid="+self.usuario+";Pwd="+self.senha+";"

	def connect(self):
		print (self.get_url_connection())




class Banco_producao:

	def __init__(self,endereco,usuario,senha,db):
		self.endereco = endereco
		self.usuario = usuario
		self.senha = senha
		self.db = db

	def get_url_connection(self):
		return "Server="+self.endereco+";Database="+self.db+";Uid="+self.usuario+";Pwd="+self.senha+";"

	def connect(self):
		print (self.get_url_connection())


class Factory:

	def build(self, tipo):
		if tipo == "local":

			return Banco().connect()
		elif tipo == "producao":
			banco = Banco_producao("producao", "raizada", "senhadificil", "dbzao")
			return banco.connect()
		else:
			print("Não reconhecemos essa conexão")

if __name__ == '__main__':

	local = Principal().instance()
	local.build("local")



	producao = Principal().instance()
	producao.build("producao")

	# Teste do singleton
	print("\n")
	print(producao)
	print(local)



