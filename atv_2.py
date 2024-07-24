import os

print("""
  # 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
  # 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
  # 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
  # 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
  # 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
""")

def exec_1():
  class Carro:
    def __init__(self, modelo, cor, ano):
      self.modelo = modelo
      self.cor = cor
      self.ano = ano

  novo_carro = Carro("Fiat Uno", "Branco", 2021)
  print(vars(novo_carro))

def exec_2():
  pass

def exec_3():
  pass

def exec_4():
  pass

def exec_5():
  pass

if __name__ == "__main__":
  escolha = input("Escolha um exercicio para ver a resolução: ")

  print("")

  match escolha:
    case "1":
      exec_1()
    case "2":
      exec_2()
    case "3":
      exec_3()
    case "4":
      exec_4()
    case "5":
      exec_5()
    case _:
      print("Opção inválida")

  input("\nPressione enter para terminar o programa")
  os.system("cls")