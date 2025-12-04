class Massa():
    def __init__(self, id_massa: str, nome: str, status_disponibilidade: bool):
        self.id_massa = id_massa
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade

class Recheio():
    def __init__(self, id_recheio: str,nome: str, status_disponibilidade: bool, valor_adc: float):
        self.id_recheio = id_recheio
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        self.valor_adc = valor_adc

class Topping():
    def __init__(self, id_topping: str, nome: str, status_disponibilidade: bool, valor_adc: float):
        self.id_topping = id_topping
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        self.valor_adc = valor_adc

class Cobertura():
    def __init__(self, id_cobertura: str, nome: str, status_disponibilidade: bool):
        self.id_cobertura = id_cobertura
        self.nome = nome
        self.status_disponibilidade = status_disponibilidade
        
