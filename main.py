from RaizCuadrada import RaizCuadrada

if __name__ == "__main__":
    numero = float(input("Ingresa un número:\n"))
    iteraciones = 10
    raiz = RaizCuadrada(numero)
    raiz.calcular_raiz(iteraciones)