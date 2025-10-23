import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


pessoa = Pessoa(nome = input("digite seu nome: "),
                email = input("digite seu E-mail: "),
                telefone = input("digite seu telefone: "),
                endereco = input("digite seu endereço: "))

os.system("cls")

print("== Exibindo dados ==")
pessoa.mostrar_dados()