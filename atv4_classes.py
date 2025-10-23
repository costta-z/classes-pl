import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str


    def somente_nome(self):
        print("== Usuario ==")
        print(f"Nome: {self.nome}")


    def mostrar_dados(self):
        print("== Exibindo dados do usuario ==")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

pessoa1 = Pessoa(nome = input("digite seu nome: "),
                email = input("digite seu E-mail: "),
                endereco = input("digite seu endereço: "))

print()

pessoa2 = Pessoa(nome = input("digite seu nome: "),
                email = input("digite seu E-mail: "),
                endereco = input("digite seu endereço: "))

os.system("cls")

pessoa1.somente_nome()
pessoa1.mostrar_dados()
print()
pessoa2.somente_nome()
pessoa2.mostrar_dados()
