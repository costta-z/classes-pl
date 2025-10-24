import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: ")
        print(f"Logadouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")


cliente1 = Cliente(nome="Marta",
                 endereco=Endereco(logradouro="Rua a.", numero=23))

print("Mostrar dados do cliente.")
cliente1.mostrar_dados()