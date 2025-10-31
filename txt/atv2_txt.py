import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: str

    def mostrar_dados(self):
        return f"Nome: {self.nome}\nAutor: {self.autor}\nCategoria: {self.categoria}\nPreço: {self.preco}"

qtd = int(input("Quantos livros você deseja cadastrar? "))
Autores = []

print("Solicitando dados do autor.")
for i in range(qtd):
    print(f"\nCadastro do autor {i + 1}")
    nome = input("Nome: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    preco = input("Preço: ")

    livro = Livro(nome, autor, categoria, preco)
    Autores.append(livro)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_livros:
    for livro in Autores:
        arquivo_livros.write(f"{livro.mostrar_dados()}\n\n")
    print("Salvo com sucesso!")
