import time

def pascal(limite):
    """
    Método que busca la cantidad de números en el triángulo de pascal que no son divisibles entre siete.
    Parametros:
    limite (int): El número de filas del triángulo que se analizan
    Retorna:
    str: Cadena con la información de la solución 
    """
    total = 1
    fila_anterior = [1]
    for num_fila in range(2, (limite+1)):
        fila = [1 for i in range(num_fila)]
        total += 2
        for i, _ in enumerate(fila[1:-1]):
            fila[i+1] = fila_anterior[i+1] + fila_anterior[i]
            if (fila[i+1] % 7 != 0):
                total += 1
        fila_anterior = fila
        # if (num_fila % 100000 == 0):
        #     print(str(num_fila))
        solucion = "Elementos dentro del triángulo no divisibles entre 7 " + \
                    "en los primeros {0} niveles es {1}".format(limite, total)
    return solucion           

def main():
    """
    Método que arranca la aplicación y mide el tiempo de ejecución.
    """
    inicio = time.clock()
    print(pascal(100))
    fin = time.clock()
    ejecucion = fin - inicio
    print("{0}s de tiempo de ejecución".format(ejecucion))
    
if __name__ == "__main__":
    main()