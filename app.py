from modelos.restaurante import Restaurante
from modelos.cardapio.sobremesa import Sobremesa
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
bebida_suco = Bebida("Suco de Melancia", 5.0, "Grande")
bebida_suco.aplicar_desconto()
prato_paozinho = Prato("Pãozinho", 2.0, "O melhor pãozinho da cidade")
prato_paozinho.aplicar_desconto()
sobremesa_pudimzinho = Sobremesa("Pudimzinho", 12.0, "Doce", "Grande", "Um baita pudim, mas você terá que competir com a arlequina")
sobremesa_pudimzinho.aplicar_desconto()
restaurante_mexicano.adicionar_no_cardapio(bebida_suco)
restaurante_mexicano.adicionar_no_cardapio(prato_paozinho)
restaurante_mexicano.adicionar_no_cardapio(sobremesa_pudimzinho)

def main():
  restaurante_mexicano.listar_cardapio()

if __name__ == "__main__":
  main()