import time

def derivar_contrasena():
    """
    Método que calcula una contraseña dada una lista de fragmentos ordenados dentro de la misma
    Retorna:
    str: Cadena con la contraseña encontrada
    """
    digitos = {}
    archivo = open('keylog.txt', 'r')
    # obtener los dígitos presentes en los fragmentos y los dígitos siguientes a cada uno
    for linea in archivo:
        linea = linea.strip('\n')
        for i, digito in enumerate(linea):
            if int(digito) not in digitos:
                digitos[int(digito)] = set()
            for digito_siguiente in linea[i+1:]:
                digitos[int(digito)].add(int(digito_siguiente))
    # print(digitos)
    # ordenar de acuerdo al tamaño del conjunto de sus dígitos subsecuentes
    contrasena = ''
    while len(digitos) > 0: 
        mayor_conjunto = -1
        valor = None
        for digito in digitos:
            if len(digitos[digito]) > mayor_conjunto:
                mayor_conjunto = len(digitos[digito])
                valor = digito
        contrasena += str(valor)
        del digitos[valor]
    solucion = "La contraseña es : {0}".format(contrasena)
    return solucion
        
def main():
    """
    Método que arranca la aplicación y mide el tiempo de ejecución.
    """
    inicio = time.clock()
    print(derivar_contrasena())
    fin = time.clock()
    ejecucion = fin - inicio
    print("{0}s de tiempo de ejecución".format(ejecucion))
    
if __name__ == "__main__":
    main()