import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"endereço: {self.endereco}")
    
    def mostrar_email_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"EMAIL: {self.email}")
        
        
        
        
pessoa1 = pessoa(nome=input("seu nome:"),
                 email=input("Digite seu email:"),
                 endereco=input("digite seu endereço: "))

os.system("cls")

print("==Mostrando dados==")
pessoa1.mostrar_dados()
print("DADOS EMAIL MARKETING")
pessoa1.mostrar_email_marketing()
