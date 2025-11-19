import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str

    def mostrar_dados(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\nCPF: {self.cpf}"

qtd = int(input("Quantos alunos você deseja cadastrar? "))
Pacientes = []

print("Solicitando dados do paciente.")
for i in range(qtd):
    print(f"\nCadastro da pessoa {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    cpf = input("CPF: ")

    paciente = Paciente(nome, idade, peso, altura,cpf)
    Pacientes.append(paciente)

print()
print("Salvando dados.")
arquivo = "dados_pacientes.csv"

with open(arquivo, "a") as arquivo_pacientes:
    for paciente in Pacientes:
        arquivo_pacientes.write(f"{paciente.mostrar_dados()}\n\n")
    print("Salvo com sucesso!")