import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    endereco: str


cliente1 = Cliente(nome="Marta", endereco="Rua A.")
cliente2 = Cliente(nome="João", endereco="Rua B.")

print("\n")
print("Mostrando apenas os nomes dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Nome: {cliente2.nome}")

print("\n")
print("Mostrando apenas os endereços dos cliente.s")
print(f"Endereço: {cliente1.endereco}")
print(f"Endereço: {cliente2.endereco}")

print("\n")
print("Mostrando todos os dados dos clientes.")
print(f"Nome: {cliente1.nome}")
print(f"Endereço: {cliente1.endereco}\n")
print(f"Nome: {cliente2.nome}")
print(f"Endereço: {cliente2.endereco}\n")