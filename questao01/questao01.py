# Implemente o método da classe Funcoes de modo que todos os testes passem

import unittest

class Funcoes:

	def funcao_a(self, n1):

		if n1 <= 100 and n1>=0:

			if n1 == 0:
				return n1

			elif n1%2 == 0:
				calc = (n1 * 2) + 1
				return calc

			elif n1%2 > 0:
				calc = (n1 - 2)
				return calc

		else:
			return "funcao so calcula ate 100"


class TestStringMethods(unittest.TestCase):
	def test_1(self):
		obj = Funcoes()
		result = obj.funcao_a(0)
		self.assertEqual(result, 0)

	def test_2(self):
		obj = Funcoes()
		result = obj.funcao_a(1)
		self.assertEqual(result, -1)
		
	def test_3(self):
		obj = Funcoes()
		result = obj.funcao_a(2)
		self.assertEqual(result, 5)

	def test_4(self):
		obj = Funcoes()
		result = obj.funcao_a(100)
		self.assertEqual(result, 201)


	def test_5(self):
		obj = Funcoes()
		result = obj.funcao_a(101)
		self.assertEqual(result, "funcao so calcula ate 100")
		
if __name__ == '__main__':
    unittest.main()
