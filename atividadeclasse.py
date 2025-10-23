import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int
    peso:float
    altura:float

print("Solicitando dados do Usuario")    
pessoa2 = pessoa(nome=input("Digite seu nome:"),
                 idade=int(input("Digite sua idade")),
                 peso=float(input("Digite seu peso")),
                 altura=float(input("Digite sua Altura")))


print("===Exibindo Dados===")
print(f"Nome:{pessoa2.nome}")
print(f"idade:{pessoa2.idade}")
print(f"Peso: {pessoa2.peso}")
print(f"Altura:{pessoa2.altura}")
print("=====================")
