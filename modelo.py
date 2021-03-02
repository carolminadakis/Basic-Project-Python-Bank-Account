class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
#Quando usamos super().__init__(atributos), estamos chamando o construtor da classe mãe
# dessa forma não precisamos repetir código recriando o mesmo construtor da classe que herdamos.
    def __str__(self):
        return f' Nome: {self._nome} - Ano: {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
            super().__init__(nome, ano)
            self.temporadas = temporadas

    def __str__(self):
           return f' Nome: {self._nome} - Ano: {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2019, 2)
panico = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
friends = Serie('friends', 1990, 10)
tbbt = Serie('the big bang theory', 2007, 12)

vingadores.dar_like()
panico.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
friends.dar_like()
friends.dar_like()
friends.dar_like()
tbbt.dar_like()
tbbt.dar_like()
tbbt.dar_like()
tbbt.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, panico, demolidor, friends, tbbt]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'The big bang theory está na playlist? {tbbt in playlist_fim_de_semana}')