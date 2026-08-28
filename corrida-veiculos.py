from abc import ABC, abstractmethod


# Classe abstrata / Interface
class Veiculo(ABC):

    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


# Classe Carro
class Carro(Veiculo):

    def acelerar(self):
        print(f"{self.modelo} está acelerando rapidamente!")


# Classe Moto
class Moto(Veiculo):

    def acelerar(self):
        print(f"{self.modelo} está acelerando com muita agilidade!")


# Classe Caminhão
class Caminhao(Veiculo):

    def acelerar(self):
        print(f"{self.modelo} está acelerando com muita potência!")


# Classe Carro Elétrico - Bônus
class CarroEletrico(Veiculo):

    def acelerar(self):
        print(f"{self.modelo} está acelerando silenciosamente com energia elétrica!")


# Lista com diferentes tipos de veículos
pista_de_corrida = [
    Carro("Toyota Corolla"),
    Moto("Honda CB 500"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


# Simulação da corrida
print("=== SIMULAÇÃO DE CORRIDA ===")

for veiculo in pista_de_corrida:
    veiculo.acelerar()