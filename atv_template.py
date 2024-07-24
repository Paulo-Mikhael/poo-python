import os

print("""""")

def exec_1():
  pass  

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