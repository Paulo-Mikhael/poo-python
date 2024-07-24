import os

print("""
  # 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
  # 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
  # 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
  # 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
  # 5 - Altere o valor do atributo nome para 'Bistrô'.
  # 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
  # 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
  # 8 - Mude o estado da instância restaurante_pizza para ativo.
  # 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
""")
      
categoria_inicial = "Mexicana"

class Restaurante:
  nome = ""
  categoria = categoria_inicial
  ativo = False 

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

def exec_1():
  restaurante_praca.nome = "Praça"
  restaurante_praca.categoria = "Italiana"
  print(vars(restaurante_praca))

def exec_2():
  restaurante_praca.nome = "Praça"
  print(f"Nome: {restaurante_praca.nome}")

def exec_3():
  print(f"O Restaurante está: {"Ativo" if restaurante_praca.ativo else "Inativo"}.")

def exec_4():
  print(f"Categoria inicial: {categoria_inicial}.")

def exec_5():
  restaurante_praca.nome = "Bistrô"
  print(f"Nome do restaurante: {restaurante_praca.nome}")

def exec_6():
  restaurante_pizza.nome = "Pizza Place"
  restaurante_pizza.categoria = "Fast Food"
  print(vars(restaurante_pizza))

def exec_7():
  restaurante_pizza.categoria = "Fast Food"
  print("É da categoria Fast Food" if restaurante_pizza.categoria == "Fast Food" else "Não é da categoria Fast Food")

def exec_8():
  restaurante_pizza.ativo = True
  restaurante_pizza.nome = "Pizza Place"
  print(f"O restaurante {restaurante_pizza.nome} está ativo")

def exec_9():
  restaurante_praca.nome = "Praça"
  restaurante_praca.categoria = "Italiana"
  print(f"Nome: {restaurante_praca.nome} | Categoria: {restaurante_praca.categoria}")


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
    case "6":
      exec_6()
    case "7":
      exec_7()
    case "8":
      exec_8()
    case "9":
      exec_9()
    case _:
      print("Opção inválida")

  input("\nPressione enter para terminar o programa")
  os.system("cls")