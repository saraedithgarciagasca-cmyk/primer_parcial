from funciones.triangulo import leerBaseAltura, calcularArea, mostrarArea
from funciones.pago_semanal import leerHorasTarifa, calcularPago, mostrarPago
from funciones.conversion_tiempo import leerSegundos, convertirTiempo, mostrarTiempo


def main():
    # Problema 1: Área de un triángulo
    leerBaseAltura()
    calcularArea()
    mostrarArea()

    # Problema 2: Pago semanal de un trabajador
    leerHorasTarifa()
    calcularPago()
    mostrarPago()

    # Problema 3: Conversión de segundos a horas, minutos y segundos
    leerSegundos()
    convertirTiempo()
    mostrarTiempo()


if __name__ == "__main__":
    main()
