class Programa:
	def __init__(self, nome, ano):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0
	def dar_like(self):
		self._likes += 1

	@property
	def likes(self):
		return self._likes

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, newName):
		self._nome = newName.title()

	def __str__(self):
		return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
	def __init__(self, nome, ano, duracao):
		super().__init__(nome, ano)
		self.duracao = duracao

	def __str__(self):
		return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
	def __init__(self, nome, ano, temporadas):
		super().__init__(nome, ano)
		self.temporadas = temporadas

	def __str__(self):
		return f'{self._nome} - {self.ano} - {self.temporadas}S - {self._likes} Likes'

class PlayList():
	def __init__(self, nome, programas):
		self.nome = nome
		self._programas = programas

	def __getitem__(self, item):
		return self._programas[item]

	def __len__(self):
		return len(self._programas)

		
		


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like();
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()





filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fds = PlayList('fds', filmes_e_series)

print(f'tamanho da PlayList: {len(playlist_fds)} programas')
	
for programa in playlist_fds:
	print(programa)

