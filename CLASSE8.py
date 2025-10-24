import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    numero: int
    cidade: str
    lograduro : str

@dataclass
class dados:
    nome: str
    email: str
    endereco: Endereco

dados1 =dados(nome="Bruno",email="BRUNO@",
               endereco=Endereco(lograduro="Rua A",cidade="Salvador",numero=5))
               

print("===MOSTRANDO DADOS===")
print(f"Nome: {dados1.nome}")
print(f"E-mail: {dados1.email}")
print(f"Endereço: {dados1.endereco.cidade},{dados1.endereco.lograduro}.{dados1.endereco.numero}")
