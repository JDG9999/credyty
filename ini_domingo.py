import time
from datetime import date

def ini_domingo(fecha_inicial, fecha_final):
    """
    Método que recorre los meses desde la fecha inicial hasta la fecha final y define si inician un domingo
    Parametros:
    fecha_inicial (date): Fecha inicial de búsqueda
    fecha_final (date): Fecha final de búsqueda
    Retorna:
    str: Cadena con la solución del problema
    """
    total = 0
    fecha = fecha_inicial
    while fecha < fecha_final:
        for mes in range(1, 13):
            fecha = fecha.replace(month=mes)
            # print(fecha)
            if (fecha.isoweekday() == 6):
                total += 1
        fecha = fecha.replace(year=fecha.year+1)
    solucion = "Meses que inician un domingo entre " + \
                "{0} y {1} es {2}".format(fecha_inicial, fecha_final, total)
    return solucion

def main():
    """
    Método que arranca la aplicación y mide el tiempo de ejecución.
    """
    inicio = time.clock()
    fecha_inicial = date(1901, 1, 1)
    fecha_final = date(2000, 12, 31)
    print(ini_domingo(fecha_inicial, fecha_final))
    fin = time.clock()
    ejecucion = fin - inicio
    print("{0}s de tiempo de ejecución".format(ejecucion))

if __name__ == "__main__":
    main()