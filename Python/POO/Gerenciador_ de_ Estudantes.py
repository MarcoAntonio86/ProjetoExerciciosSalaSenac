'''Crie uma classe chamada `Estudante` que represente um estudante. O estudante deve ter os 
seguintes atributos e métodos:
- Atributos:
 - `nome`: O nome do estudante.
 - `matricula`: A matrícula do estudante.
 - `notas`: Uma lista de notas do estudante.
- Métodos:
 - `adicionar_nota(self, nota)`: Um método que permite adicionar uma nota à lista de notas do 
estudante.
 - `calcular_media(self)`: Um método que calcula e retorna a média das notas do estudante.
Crie objetos da classe `Estudante`, adicione notas a eles e calcule suas médias.'''

class Estudante:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    

estudante1 = Estudante('Alice', '233', [])
estudante1.adicionar_nota(20)
estudante1.adicionar_nota(30)
estudante1.adicionar_nota(40)
estudante1.adicionar_nota(50)


print(estudante1.nome, estudante1.matricula, estudante1.calcular_media())