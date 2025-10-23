import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class dados:
    nome: str
    email: str
    endereco: str
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")
    
    def mostrar_so_nome(self):
        print(f"NOME{self.nome}")
        
    
    
pessoa1 = dados(nome=input("Digite seu nome: "),
                email=input("Digite seu email: "),
                endereco=input("Digite seu endereço: "))

pessoa2 = dados(nome=input("Digite seu nome: "),
                email=input("Digite seu email: "),
                endereco=input("Digite seu endereço: "))

os.system("cls")

print("=== Mostrando Dados ===")
pessoa1.mostrar_dados()
pessoa1.mostrar_so_nome()
print("=====Mostrar dados da pessoa 2=====")
pessoa2.mostrar_dados()
pessoa2.mostrar_so_nome
