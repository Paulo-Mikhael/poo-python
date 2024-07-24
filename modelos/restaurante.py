from modelos.avaliacao import Avaliacao

class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria
    self._ativo = False 
    self._avaliacao = []
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f"\nNome: {self._nome} \nCategoria: {self._categoria}"
  
  @classmethod
  def listar_restaurantes(cls):
    for restaurante in cls.restaurantes:
      print(f"\nNome: {restaurante._nome} \nCategoria: {restaurante._categoria} \nAtivo: {restaurante.ativo} \nAvaliação: {restaurante.media_avaliacoes}")
  
  @property
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

Restaurante.listar_restaurantes()