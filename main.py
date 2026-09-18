#!/usr/bin/env python3
"""
main.py

Implementa uma hierarquia de classes para Veículo com encapsulamento,
polimorfismo e um menu interativo em terminal para cadastrar e simular
aluguel de `Carro` e `Moto`.

Uso: python main.py
"""
from typing import List


class BusinessRuleError(Exception):
    """Exceção para regras de negócio (validações específicas)."""


class Veiculo:
    """Superclasse para veículos com atributos privados e propriedades.

    Atributos privados:
    - __modelo: str
    - __placa: str
    - __valor_diaria: float
    """

    def __init__(self, modelo: str, placa: str, valor_diaria: float):
        # Use setters para validação centralizada
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise BusinessRuleError("Modelo não pode ser vazio e deve ser texto.")
        self.__modelo = value.strip()

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise BusinessRuleError("Placa não pode ser vazia e deve ser texto.")
        self.__placa = value.strip().upper()

    @property
    def valor_diaria(self) -> float:
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, value):
        try:
            valor = float(value)
        except (TypeError, ValueError):
            raise ValueError("Valor da diária deve ser um número válido.")
        if valor <= 0:
            raise BusinessRuleError("Valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    def calcular_aluguel(self, dias: int) -> float:
        """Calcula aluguel básico: dias * valor_diaria.

        Valida regras básicas de negócio (dias > 0).
        """
        try:
            dias_int = int(dias)
        except (TypeError, ValueError):
            raise ValueError("Dias deve ser um número inteiro positivo.")
        if dias_int <= 0:
            raise BusinessRuleError("Número de dias deve ser maior que zero.")
        return dias_int * self.valor_diaria

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: Modelo={self.modelo}, Placa={self.placa}, Diária={self.valor_diaria:.2f}"


class Carro(Veiculo):
    """Subclasse de Veiculo com atributo específico `portas`.

    O aluguel de `Carro` adiciona uma taxa fixa de limpeza de 50.00.
    """

    def __init__(self, modelo: str, placa: str, valor_diaria: float, portas: int, possui_ar: bool = False):
        super().__init__(modelo, placa, valor_diaria)
        self.portas = portas
        self.possui_ar = possui_ar

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, value):
        try:
            p = int(value)
        except (TypeError, ValueError):
            raise ValueError("Portas deve ser um número inteiro.")
        if p <= 0:
            raise BusinessRuleError("Portas deve ser maior que zero.")
        self.__portas = p

    @property
    def possui_ar(self) -> bool:
        return self.__possui_ar

    @possui_ar.setter
    def possui_ar(self, value):
        # Aceita bool ou representação textual
        if isinstance(value, bool):
            self.__possui_ar = value
            return
        if isinstance(value, str):
            val = value.strip().lower()
            if val in ("s", "sim", "y", "yes", "1"):
                self.__possui_ar = True
                return
            if val in ("n", "nao", "não", "no", "0"):
                self.__possui_ar = False
                return
        raise BusinessRuleError("Valor inválido para 'possui_ar'. Use 's'/'n' ou booleano.")

    def calcular_aluguel(self, dias: int) -> float:
        base = super().calcular_aluguel(dias)
        taxa_limpeza = 50.00
        return base + taxa_limpeza

    def __str__(self) -> str:
        ar = "Sim" if self.possui_ar else "Não"
        return f"{super().__str__()}, Portas={self.portas}, Ar-condicionado={ar}"


class Moto(Veiculo):
    """Subclasse de Veiculo com atributo específico `cilindradas`.

    O aluguel de `Moto` recebe 10% de desconto no total.
    """

    def __init__(self, modelo: str, placa: str, valor_diaria: float, cilindradas: int):
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    @property
    def cilindradas(self) -> int:
        return self.__cilindradas

    @cilindradas.setter
    def cilindradas(self, value):
        try:
            c = int(value)
        except (TypeError, ValueError):
            raise ValueError("Cilindradas deve ser um número inteiro.")
        if c <= 0:
            raise BusinessRuleError("Cilindradas deve ser maior que zero.")
        self.__cilindradas = c

    def calcular_aluguel(self, dias: int) -> float:
        base = super().calcular_aluguel(dias)
        desconto = 0.10
        return base * (1 - desconto)

    def __str__(self) -> str:
        return f"{super().__str__()}, Cilindradas={self.cilindradas}"


# Lista centralizada de veículos heterogêneos
veiculos: List[Veiculo] = []


def cadastrar_carro():
    """Solicita dados do carro e registra na lista centralizada."""
    modelo = input("Modelo do carro: ").strip()
    placa = input("Placa: ").strip()
    diaria = input("Valor da diária: ").strip()
    portas = input("Quantidade de portas: ").strip()
    possui_ar = input("Possui ar-condicionado? (s/n): ").strip()

    # Verifica duplicidade de placa
    if any(v.placa == placa.upper() for v in veiculos):
        raise BusinessRuleError("Já existe um veículo cadastrado com essa placa.")

    carro = Carro(modelo=modelo, placa=placa, valor_diaria=diaria, portas=portas, possui_ar=possui_ar)
    veiculos.append(carro)
    print("Carro cadastrado com sucesso.")


def cadastrar_moto():
    """Solicita dados da moto e registra na lista centralizada."""
    modelo = input("Modelo da moto: ").strip()
    placa = input("Placa: ").strip()
    diaria = input("Valor da diária: ").strip()
    cilindradas = input("Cilindradas: ").strip()

    if any(v.placa == placa.upper() for v in veiculos):
        raise BusinessRuleError("Já existe um veículo cadastrado com essa placa.")

    moto = Moto(modelo=modelo, placa=placa, valor_diaria=diaria, cilindradas=cilindradas)
    veiculos.append(moto)
    print("Moto cadastrada com sucesso.")


def listar_veiculos():
    """Exibe todos os veículos cadastrados."""
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return
    for i, v in enumerate(veiculos, start=1):
        print(f"{i}. {v}")


def simular_aluguel():
    """Simula o aluguel de um veículo a partir da placa e dias informados."""
    busca = input("Informe a placa do veículo a alugar: ").strip().upper()
    if not busca:
        raise ValueError("Placa não pode ser vazia para busca.")

    encontrados = [v for v in veiculos if v.placa == busca]
    if not encontrados:
        raise KeyError("Veículo não encontrado para a placa informada.")
    veiculo = encontrados[0]

    dias = input("Quantidade de dias: ").strip()
    total = veiculo.calcular_aluguel(dias)
    print(f"Aluguel de {veiculo.modelo} (placa {veiculo.placa}) por {int(dias)} dias: R$ {total:.2f}")


def menu():
    """Loop principal do menu interativo com tratamento robusto de exceções."""
    opcao_text = (
        "\nEscolha uma opção:\n"
        "1 - Cadastrar Carro\n"
        "2 - Cadastrar Moto\n"
        "3 - Listar Frota\n"
        "4 - Simular Aluguel de Veículo\n"
        "5 - Sair\n"
        "Opção: "
    )

    while True:
        try:
            escolha = input(opcao_text).strip()
            if not escolha:
                print("Opção vazia. Informe um número entre 1 e 5.")
                continue
            try:
                opcao = int(escolha)
            except ValueError:
                raise ValueError("Opção deve ser um número inteiro entre 1 e 5.")

            if opcao == 1:
                cadastrar_carro()
            elif opcao == 2:
                cadastrar_moto()
            elif opcao == 3:
                listar_veiculos()
            elif opcao == 4:
                simular_aluguel()
            elif opcao == 5:
                print("Saindo. Obrigado!")
                break
            else:
                print("Opção inválida. Escolha entre 1 e 5.")

        except BusinessRuleError as bre:
            print(f"Erro de negócio: {bre}")
        except KeyError as ke:
            print(f"Busca inválida: {ke}")
        except ValueError as ve:
            print(f"Entrada inválida: {ve}")
        except KeyboardInterrupt:
            print("\nInterrupção por teclado. Saindo...")
            break
        except Exception as e:
            # Captura qualquer exceção inesperada para evitar crash
            print(f"Ocorreu um erro inesperado: {e}")
        else:
            # Caso nenhuma exceção ocorra
            pass
        finally:
            # Espaçamento visual entre iterações
            print("-" * 40)


if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"Erro crítico: {e}")
