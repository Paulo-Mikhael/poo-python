import json
import requests

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

def chamar_api():
  url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
  response = requests.get(url)
  dados_do_restaurante = {}

  if response.status_code == 200:
    dados_json = response.json()

    for item in dados_json:
      nome_do_restaurante = item["Company"]
      if nome_do_restaurante not in dados_do_restaurante:
        dados_do_restaurante[nome_do_restaurante] = []
      dados_do_restaurante[nome_do_restaurante].append({
        "item": item["Item"],
        "price": item["price"],
        "description": item["description"]
      })
    
    print(response)
  else:
    print(f"Ocorreu o erro de número {response.status_code}")

  for nome_restaurante, dados in dados_do_restaurante.items():
    nome_do_arquivo = f"{nome_restaurante}.json"
    with open(nome_do_arquivo, "w") as arquivo_restaurante:
      json.dump(dados, arquivo_restaurante, indent=2)

def main():
  chamar_api()

if __name__ == "__main__":
  main()