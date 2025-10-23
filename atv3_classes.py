import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print("== Dados de entrega ==")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print("== Dados de E-mail makerting ==")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")


pessoa = Pessoa(nome = input("digite seu nome: "),
                email = input("digite seu E-mail: "),
                endereco = input("digite seu endereço: "))

os.system("cls")

pessoa.dados_entrega()
print()
pessoa.dados_email_marketing()