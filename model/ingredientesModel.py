class Massa():
    def __init__(self, nome: str, status_disponibilidade: bool):
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade

class Recheio():
    def __init__(self, nome: str, status_disponibilidade: bool, valor_adcional: float):
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        self.valor_adcional = valor_adcional

class Topping():
    def __init__(self, nome: str, status_disponibilidade: bool):
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade

class Cobertura():
    def __init__(self, nome: str, status_disponibilidade: bool):
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        
