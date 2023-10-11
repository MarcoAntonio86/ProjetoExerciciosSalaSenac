'''Desenvolva um simulador de jogo RPG em Python. Crie classes para representar
personagens, monstros e itens do jogo. Implemente métodos para ações como atacar,
defender, usar itens e ganhar experiência. O jogo deve permitir a criação de personagens,
batalhas contra monstros e aprimoramento de habilidades à medida que o personagem ganha
experiência.'''


import random

class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.experiencia = 0

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

    def defender(self):
        print(f"{self.nome} se defende e ganha +2 de defesa!")
        self.defesa += 2

    def usar_item(self, item):
        if item == "Poção de Vida":
            self.vida += 20
            print(f"{self.nome} usa uma Poção de Vida e recupera 20 pontos de vida!")
        else:
            print(f"{self.nome} não pode usar este item.")

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        print(f"{self.nome} ganha {quantidade} de experiência!")

class Monstro:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

def batalha(personagem, monstro):
    print(f"{personagem.nome} enfrenta {monstro.nome}!")
    while personagem.vida > 0 and monstro.vida > 0:
        if random.random() < 0.5:
            personagem.atacar(monstro)
        else:
            monstro.atacar(personagem)
        if personagem.vida > 0:
            personagem.defender()
        if monstro.vida > 0:
            monstro.atacar(personagem)
    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado por {monstro.nome}.")
    else:
        print(f"{personagem.nome} derrotou {monstro.nome} e ganhou a batalha!")
        experiencia_ganha = random.randint(10, 30)
        personagem.ganhar_experiencia(experiencia_ganha)


heroi = Personagem("Herói", "Guerreiro", 100, 20, 10)
monstro = Monstro("Monstro", 80, 15, 5)


batalha(heroi, monstro)


print(f"{heroi.nome}: Vida = {heroi.vida}, Experiência = {heroi.experiencia}")
