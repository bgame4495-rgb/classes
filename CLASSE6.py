import os
os.system ("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str
    
    def mostrar_dados(self):
        print(f"NOME: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"telefone: {self.telefone}")

    def dados_sms_marketing(self):
        print(f"telefone: {self.telefone}")

lista_de_pessoas = []

for i in range(3):
    dados_cliente = Pessoa(nome=input("Digite seu nome: "),
                           cpf= input("Digite seu CPF"),
                           telefone=input("Digite seu telefone: "))
    lista_de_pessoas.append(dados_cliente)
    os.system("cls")

for cliente in lista_de_pessoas:
    cliente.mostrar_dados()
