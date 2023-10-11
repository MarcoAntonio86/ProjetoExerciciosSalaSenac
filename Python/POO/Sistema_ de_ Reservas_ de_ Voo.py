'''Crie um sistema de reservas de voo em Python. Crie classes para representar voos,
passageiros e reservas. Implemente métodos para verificar a disponibilidade de voos, fazer
reservas, cancelar reservas e emitir bilhetes de embarque. O sistema deve permitir que os
passageiros façam reservas e consultem suas informações de voo.'''

class Voo:
    def __init__(self, numero_voo, capacidade):
        self.numero_voo = numero_voo
        self.capacidade = capacidade
        self.passageiros = []

    def assentos_disponiveis(self):
        return self.capacidade - len(self.passageiros)

    def reservar_voo(self, passageiro):
        if self.assentos_disponiveis() > 0:
            self.passageiros.append(passageiro)
            return f"Reserva confirmada para o voo {self.numero_voo} para {passageiro.nome}."
        else:
            return f"Desculpe, não há mais assentos disponíveis no voo {self.numero_voo}."

    def cancelar_reserva(self, passageiro):
        if passageiro in self.passageiros:
            self.passageiros.remove(passageiro)
            return f"Reserva cancelada para o voo {self.numero_voo} de {passageiro.nome}."
        else:
            return f"{passageiro.nome} não tem uma reserva no voo {self.numero_voo}."

    def informacoes_passageiro(self, passageiro):
        if passageiro in self.passageiros:
            return f"Informações do voo {self.numero_voo} para {passageiro.nome}:"
        else:
            return f"{passageiro.nome} não tem uma reserva no voo {self.numero_voo}."


class Passageiro:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


# Exemplo de uso do sistema de reservas de voo:

# Criação de voos
voo1 = Voo("AA101", 100)
voo2 = Voo("BA202", 150)

# Criação de passageiros
passageiro1 = Passageiro("Alice")
passageiro2 = Passageiro("Bob")

# Reservas
print(voo1.reservar_voo(passageiro1))  # Reserva confirmada para o voo AA101 para Alice.
print(voo1.reservar_voo(passageiro2))  # Reserva confirmada para o voo AA101 para Bob.
print(voo2.reservar_voo(passageiro1))  # Desculpe, não há mais assentos disponíveis no voo BA202.

# Cancelar reserva
print(voo1.cancelar_reserva(passageiro2))  # Reserva cancelada para o voo AA101 de Bob.

# Informações do passageiro
print(voo1.informacoes_passageiro(passageiro1))  # Informações do voo AA101 para Alice.
print(voo1.informacoes_passageiro(passageiro2))  # Bob não tem uma reserva no voo AA101.

