from modelos.restaurante import Restaurante

restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_mexicano.receber_avaliacao("Paulo", 5)
restaurante_mexicano.receber_avaliacao("Miguel", 3)
restaurante_mexicano.receber_avaliacao("Bentes", 5)

def main():
  Restaurante.listar_restaurantes()

if __name__ == "__main__":
  main()