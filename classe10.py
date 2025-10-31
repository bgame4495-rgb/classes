import os 
os.system("cls")
from dataclasses import dataclass

@dataclass 
class Autor: 
    nome: str 
    biografia: str

@dataclass
class livro:
    titulo: str
    ano: int
    autor: Autor

    def mostrar_resultado(self): 
        print(f"Autor: {self.autor.nome}")
        print(f"Biografia: {self.autor.biografia}")
        print(f"Livro: {self.titulo}")
        print(f"Data de publicação: {self.ano}")

pessoa= livro(titulo=input("Digite o titulo do livro: "),
              ano=int(input("Digite o seu ano de lançamento: ")),
              autor=Autor(nome=input("Digite o nome do autor: "),
                          biografia=input("Digite a biografia: ")))

os.system("cls")
print("\n===MOSTRAR DETALHES DO LIVRO===")
pessoa.mostrar_resultado()
