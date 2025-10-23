import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class dados:
    nome: str
    email:str
    telefone:str
    cep: str

dados1= dados(nome=input("Digite seu nome: "),
              email=input("Digite seu email: "),
              telefone=input("Digite seu telefone:"),
              cep=input("Digite seu endereço: "))

print("===Exibindo Dados===")
print(f"nome={dados1.nome}")
print(f"email= {dados1.email}")           
print(f"telefone: {dados1.telefone}")
print(f"endereço: {dados1.cep}")
