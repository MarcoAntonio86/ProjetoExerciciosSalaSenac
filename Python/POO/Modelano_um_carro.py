'''Crie uma classe chamada `Carro` que represente um veículo. O carro deve ter os seguintes 
atributos e métodos:
- Atributos:
 - `marca`: A marca do carro.
 - `modelo`: O modelo do carro.
 - `ano`: O ano de fabricação do carro.
 - `velocidade`: A velocidade atual do carro (inicialmente, 0).
- Métodos:
 - `acelerar(self, incremento)`: Um método que aumenta a velocidade do carro pelo valor do 
incremento.
 - `frear(self, decremento)`: Um método que diminui a velocidade do carro pelo valor do 
decremento.
 - `informacoes(self)`: Um método que exibe as informações do carro, incluindo marca, 
modelo, ano e velocidade atual.
Crie um objeto da classe `Carro`, realize algumas operações de aceleração e frenagem, e exiba 
as informações do carro.'''


class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
    
    def acelerar(self, incremento):
        self.velocidade += incremento
    
    def frear(self, decremento):
        self.velocidade -= decremento
    
    def informacoes(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nVelocidade: {self.velocidade}')

carro1 = Carro('Fiat', 'Uno', 2010, 0)
carro1.acelerar(10)
carro1.frear(5)
carro1.informacoes()