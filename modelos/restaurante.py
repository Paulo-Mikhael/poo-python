from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria
    self._ativo = False 
    self._avaliacao = []
    self._cardapio = []
    Restaurante.restaurantes.append(self)

  def __str__(self): # Imprime esse valor se for chamado como texto
    return f"\nNome: {self._nome} \nCategoria: {self._categoria}"
  
  @classmethod # Uma função é declarada como classmethod quando é preciso chamar a classe na lógica da função
  def listar_restaurantes(cls):
    for restaurante in cls.restaurantes:
      print(f"\nNome: {restaurante._nome} \nCategoria: {restaurante._categoria} \nAtivo: {restaurante.ativo} \nAvaliação: {restaurante.media_avaliacoes}")
  
  @property # Uma função é declarada como propriedade quando o retorno é um valor para ser usado no código
  def ativo(self):
    return '✔️' if self._ativo else '❌'

  @property
  def media_avaliacoes(self):
    if not self._avaliacao:
      return '--'
    
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
    quantidade_notas = len(self._avaliacao)
    media = round(soma_das_notas / quantidade_notas, 1)
    return media
  
  def alternar_estado(self):
    self._ativo = not self._ativo
  
  def receber_avaliacao(self, cliente, nota):
    if nota > -1 and nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)

  def adicionar_no_cardapio(self, item):
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)

  def listar_cardapio(self):
    print(f"Cardápio do restaurante {self._nome}\n")
    for i, item in enumerate(self._cardapio, start=1):
      mensagem = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco}"
      tipo_item = type(item)
      
      if tipo_item == Sobremesa:
        mensagem += f" | Tipo: {item._tipo} | Tamanho: {item._tamanho} | Descrição: {item._descricao}"
      elif tipo_item == Bebida:
        mensagem += f" | Tamanho: {item._tamanho}"
      elif tipo_item == Prato:
        mensagem += f" | Descrição: {item._descricao}"

      print(mensagem)