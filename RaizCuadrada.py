class RaizCuadrada:
    def __init__(self, a: float):
        self.a = a
        self.x = 1.0

    def calcular_raiz(self, iteraciones: int):
        for k in range(1, iteraciones + 1):
            self.x = (self.x + self.a / self.x) / 2
            print(f"La raíz después de {k} iteraciones es {self.x}")