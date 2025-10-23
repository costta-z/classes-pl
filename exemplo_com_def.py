import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
 

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


pessoa1 = Pessoa(nome = input("digite seu nome: "),
                idade = input("digite sua iade: "))

pessoa2 = Pessoa(nome = input("digite seu nome: "),
                idade = input("digite sua iade: "))


os.system("cls")

print("== Exibindo dados ==")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()