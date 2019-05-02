import time

def tripleta(suma):
    """
    Método que busca tres números que satisfacen la tripleta de pitágoras y una suma dada.
    Parametros:
    suma (int): La suma que deben satisfacer los números de la tripleta
    Retorna:
    str: Cadena con la información de los números de la tripleta y su producto (si existen)
    """
    for a in range(1, suma):
        for b in range((a+1), suma):
            c = (a**2 + b**2)**(0.5)
            if a+b+c == suma:
                producto = a*b*c
                solucion = "a={0}, b={1}, c={2}, producto={3}".format(a,b,c,producto)
                return solucion
    return "La solución no existe"

def main():
    """
    Método que arranca la aplicación y mide el tiempo de ejecución.
    """
    inicio = time.clock()
    print(tripleta(1000))
    fin = time.clock()
    ejecucion = fin - inicio
    print("{0}s de tiempo de ejecución".format(ejecucion))
    
if __name__ == "__main__":
    main()