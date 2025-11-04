import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Endereco:
    cidade: str
    logadouro: str
    numero: int

@dataclass
class Cliente:
    cod: int
    nome: str
    email: str
    telefone: str
    endereco: Endereco

    def mostrar_dados(self):
        return (
        f"Código: Cliente {self.cod}\n"
        f"Nome: {self.nome}\n"
        f"E-mail: {self.email}\n"
        f"Telefone: {self.telefone}\n"
        f"Cidade: {self.endereco.cidade}\n"
        f"Logadouro: {self.endereco.logadouro}\n"
        f"Numero: {self.endereco.numero}"
        )

def obter_ultimo_codigo(arquivo):
    ultimo = 0
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq:
            for linha in arq:
                if linha.startswith("Código: Cliente"):
                    num = int(linha.replace("Código: Cliente", "").strip())
                    ultimo = num
    return ultimo

arquivo = "dados_clientes.txt"
cod = obter_ultimo_codigo(arquivo)

qtd = int(input("Quantas pessoas você deseja cadastrar? "))
clientes = []

for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    cod += 1
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")
    logadouro = input("Logadouro: ")
    numero = int(input("Numero: "))

    endereco = Endereco(cidade,logadouro,numero)
    cliente = Cliente(cod, nome, email, telefone, endereco)
    clientes.append(cliente)

print("\nSalvando dados...")

with open(arquivo, "a") as arquivo_clientes:
    for cliente in clientes:
        arquivo_clientes.write(f"{cliente.mostrar_dados()}\n\n")

print("Salvo com sucesso!")
