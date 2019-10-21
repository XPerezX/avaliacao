# 
# O sistema hoje possui uma classe para se conectar ao banco de dados local
# Foi feito o deploy do sistema para a aws, mas a string de conexão mudou
# Vocês tem que prover uma nova classe de conexão com o banco e utilizar 
# algum padrão de projeto para flexibilizar as conexões com o banco
# o ideal é que a classe principal não saiba em qual banco ele está conectando
# e que so haja uma instancia de cada classe de conexão ao banco

class Principal:
	def __init__(self):
		banco = Banco()
		banco.connect()

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

if __name__ == '__main__':
	principal = Principal()
    
