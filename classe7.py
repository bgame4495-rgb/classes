import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logdradouro: str
    numero: int

@dataclass
class cliente:
    nome: str
    endereco: Endereco

cliente1= cliente(nome="marte", 
                  endereco=Endereco(logdradouro="Rua a",numero=23))
                

print("mostrar dados de cliente")
print(f"nome: {cliente1.nome}")
print(f"endereço {cliente1.endereco.logdradouro}")
print(f"numero: {cliente1.endereco.numero}")
