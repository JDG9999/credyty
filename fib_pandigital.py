import time

def fibonacci_pandigital():
    """
    Método que define si una cadena que representa un número es pandigital.
    Retorna:
    str: Cadena con la información de la posición k del número, y el número en cuestión.
    """
    a = 1
    b = 1
    num = 2
    k = 3
    while True:
        a, b = b, num
        num = a + b
        k = k + 1
        # print("Probando k=" + str(k))
        inicia_pandigital = es_pandigital(str(num)[:9])
        if (inicia_pandigital):
            termina_pandigital = es_pandigital(str(num)[-9:])
            if (termina_pandigital):
                solucion = "k={0}, numero={1}".format(k, num)
                return solucion
        # if (k % 10000 == 0):
        #     print("k=" + str(k))
        # if (k > 500000):
        #     return "*Error*"

def es_pandigital(numero):
    """
    Método que define si una cadena que representa un número es pandigital.
    Parámetros:
    numero (str): cadena que representa un número.
    Retorna:
    bool: Si el número es pandigital o no.
    """
    return not '123456789'.strip(numero)

def main():
    """
    Método que arranca la aplicación y mide el tiempo de ejecución.
    """
    inicio = time.clock()
    print(fibonacci_pandigital())
    fin = time.clock()
    ejecucion = fin - inicio
    print("{0}s de tiempo de ejecución".format(ejecucion))
    
if __name__ == "__main__":
    main()