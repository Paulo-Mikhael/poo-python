# Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo.

class Musica:
  musicas = []

  def __init__(self, nome: str, artista: str, duracao: int):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    Musica.musicas.append(self)

  def __str__(self):
    return str(vars(self))

  def listar_musicas():
    for musica in Musica.musicas:
      print(f"\nNome da música: {musica.nome} \nArtista: {musica.artista} \nDuração: {musica.duracao}")

  def procurar_por_nome(nome):
    for musica in Musica.musicas:
      if musica.nome == nome:
        return musica
      
    return f"Música '{nome}' não encontrada"

buda = Musica("Iluminado", "M4rkim", 180)
rick_morty = Musica("Tipo Rick e Morty", "VMZ", 170)
tesla = Musica("Rap da Akatsuki", "7MZ", 620)

musica_pega = Musica.procurar_por_nome("Iluminado")

print(musica_pega)