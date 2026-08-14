class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
    
    def calcular_bonus(self):
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def calcular_bonus(self):
        return super().calcular_bonus() + 1000


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas
    
    def calcular_bonus(self):
        return self.total_vendas * 0.10


# Exemplo de uso:
if __name__ == "__main__":
    func = Funcionario("João", 2000)
    gerente = Gerente("Maria", 3000)
    vendedor = Vendedor("Pedro", 2000, 5000)
    
    print(f"{func.nome} - Bônus: R$ {func.calcular_bonus():.2f}")
    print(f"{gerente.nome} - Bônus: R$ {gerente.calcular_bonus():.2f}")
    print(f"{vendedor.nome} - Bônus: R$ {vendedor.calcular_bonus():.2f}")
