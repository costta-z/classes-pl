import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: str

pessoa = Pessoa(nome = input("digite seu nome: "),
                email = input("digite seu E-mail: "),
                telefone = int(input("digite seu telefone: ")),
                endereco = input("digite seu endereço: "))

os.system("cls")

print("\n= Exibindo dados =")
print(f"Nome: {pessoa.nome}\nEmail: {pessoa.email}\nTelefone: {pessoa.telefone}\nEndereço: {pessoa.endereco}")



