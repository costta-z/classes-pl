import os
from dataclasses import dataclass

os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco: str

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str


def cadastrar_clientes(qtd):
    clientes = []
    for i in range(qtd):
        print(f"\nCadastro do cliente {i + 1}")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        clientes.append(Cliente(nome, data_nascimento, endereco))
    return clientes


def cadastrar_funcionarios(qtd_func):
    funcionarios = []
    for i in range(qtd_func):
        print(f"\nCadastro do funcionário {i + 1}")
        nome = input("Nome: ")
        data_admissao = input("Data de admissão: ")
        matricula = input("Matrícula: ")
        endereco = input("Endereço: ")
        funcionarios.append(Funcionario(nome, data_admissao, matricula, endereco))
    return funcionarios


def salvar_dados_em_csv(arquivo, cabecalho, linhas):
    novo_arquivo = not os.path.exists(arquivo)

    with open(arquivo, "a", encoding="utf-8") as file:
        if novo_arquivo:
            file.write(cabecalho)

        for linha in linhas:
            file.write(linha + "\n")

def mostrar_dados_clientes(arquivo):
    print("\n===== CLIENTES CADASTRADOS =====")
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            next(file)  # pula o cabeçalho
            for linha in file:
                nome, nasc, end = linha.strip().split(",")
                print(f"\nNome: {nome}\nData de nascimento: {nasc}\nEndereço: {end}")
    except FileNotFoundError:
        print("Arquivo de clientes não encontrado.")


def mostrar_dados_funcionarios(arquivo):
    print("\n===== FUNCIONÁRIOS CADASTRADOS =====")
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            next(file)  # pula o cabeçalho
            for linha in file:
                nome, adm, matricula, end = linha.strip().split(",")
                print(f"\nNome: {nome}\nAdmissão: {adm}\nMatrícula: {matricula}\nEndereço: {end}")
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")


def main():
    qtd_clientes = int(input("Quantos clientes deseja cadastrar? "))
    clientes = cadastrar_clientes(qtd_clientes)

    qtd_funcionarios = int(input("Quantos funcionários deseja cadastrar? "))
    funcionarios = cadastrar_funcionarios(qtd_funcionarios)

    arquivo_clientes = "dados_clientes.csv"
    arquivo_funcionarios = "dados_funcionarios.csv"

    salvar_dados_em_csv(
        arquivo_clientes,
        "Nome,DataNascimento,Endereco\n",
        [f"{c.nome},{c.data_nascimento},{c.endereco}" for c in clientes]
    )

    salvar_dados_em_csv(
        arquivo_funcionarios,
        "Nome,DataAdmissao,Matricula,Endereco\n",
        [f"{f.nome},{f.data_admissao},{f.matricula},{f.endereco}" for f in funcionarios]
    )

    mostrar_dados_clientes(arquivo_clientes)
    mostrar_dados_funcionarios(arquivo_funcionarios)


if __name__ == "__main__":
    main()
