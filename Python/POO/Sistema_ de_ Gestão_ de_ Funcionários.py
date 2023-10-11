'''Crie um sistema de gestão de funcionários em Python. Crie classes para representar
funcionários, como `Funcionário` e `Gerente`, com atributos como nome, ID, salário etc.
Implemente métodos para calcular salários, gerenciar promoções, contratações e demissões. O
sistema deve permitir a criação, modificação e consulta de informações dos funcionários.'''

class Funcionario:
    def __init__(self, nome, id, salario):
        self.nome = nome
        self.id = id
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def aumento(self, porcentagem):
        aumento = self.salario * (porcentagem / 100)
        self.salario += aumento

    def demitir(self):
        self.salario = 0

class Gerente(Funcionario):
    def __init__(self, nome, id, salario):
        super().__init__(nome, id, salario)

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)

    def demitir(self, funcionario):
        self.funcionarios.remove(funcionario)
        print(f'O funcionário {funcionario.nome} foi demitido.')

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f'ID: {funcionario.id}, Nome: {funcionario.nome}, Salário: {funcionario.salario}')

funcionario1 = Funcionario('Joaquim', 1, 5000)
funcionario2 = Funcionario('Maria', 2, 6000)
funcionario3 = Funcionario('Pedro', 3, 7000)
gerente1 = Gerente('Marco', 4, 9000)

empresa = Empresa()
empresa.contratar(funcionario1)
empresa.contratar(funcionario2)
empresa.contratar(funcionario3)
empresa.contratar(gerente1)

print("Funcionários na empresa:")
empresa.listar_funcionarios()

empresa.demitir(funcionario1)

print("\nFuncionários após demissão:")
empresa.listar_funcionarios()

aumento = Funcionario('Maria', 2, 6000)
aumento.aumento(10)

print("\nSalário de Maria após aumento:")
print(f'Nome: {aumento.nome}, Salário: {aumento.salario}')




