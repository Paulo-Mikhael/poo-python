from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/")
def inicio():
  return {"Documentação": "/docs"}

@app.get("/api/hello")
def hello_world():
  """
    Mensagem íncrivel do universo da programação
  """
  return {"Hello": "World"}

@app.get("/api/restaurantes")
def get_restaurantes(restaurante: str = Query(None)):

  url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
  response = requests.get(url)
  dados_do_restaurante = {}

  if response.status_code == 200:
    dados_json = response.json()

    if restaurante is None:
      return {"Dados": dados_json}
    
    print(restaurante)

    for item in dados_json:
      nome_do_restaurante = item["Company"]

      if nome_do_restaurante == restaurante:
        if nome_do_restaurante not in dados_do_restaurante:
          dados_do_restaurante[restaurante] = []

        dados_do_restaurante[restaurante].append({
          "item": item["Item"],
          "price": item["price"],
          "description": item["description"]
        })
    return {"Restaurante": restaurante, "Cardapio": dados_do_restaurante}
  else:
    return {"Erro": f"{response.status_code} - {response.text}"}