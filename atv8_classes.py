import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor  

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")

print(f"\nCadastro da pessoa ")
nome = input("Nome do autor: ")
biografia = input("Biografia do autor: ")
titulo = input("Título do livro: ")
ano = int(input("Ano de publicação: "))

autor = Autor(nome, biografia)
livro = Livro(titulo, ano, autor)

os.system("cls")
livro.exibir_detalhes()
