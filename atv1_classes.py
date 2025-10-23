import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa = Pessoa(nome = input("digite seu nome:"),
                idade = int(input("digite sua idade:")),
                peso = float(input("digite seu peso:")),
                altura = float(input("digite sua altura:")))

print("\n= Exibindo dados =")
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso}\nAltura: {pessoa.altura}")



