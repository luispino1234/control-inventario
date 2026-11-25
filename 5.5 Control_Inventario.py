"""
Programa: Control de inventario
Problema 3 - Fase 5
Curso: Fundamentos de Programación - UNAD

Calcula la cantidad exacta de unidades que se deben solicitar para que
cada artículo alcance su stock mínimo requerido.
"""


def calcular_reposicion(stock_actual, stock_minimo):
    """Retorna la cantidad que se debe pedir para alcanzar el stock mínimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def mostrar_reabastecimiento(inventario):
    """Recorre la matriz y muestra el resultado para cada artículo."""
    print("\nREPORTE DE REABASTECIMIENTO")
    print("-" * 76)
    print(
        f"{'CÓDIGO':<10} | {'ARTÍCULO':<16} | "
        f"{'STOCK ACTUAL':>12} | {'CANTIDAD A PEDIR':>16}"
    )
    print("-" * 76)

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad = calcular_reposicion(stock_actual, stock_minimo)
        print(
            f"{codigo:<10} | {nombre:<16} | "
            f"{stock_actual:>12} | {cantidad:>16}"
        )

    print("-" * 76)


def main():
    # Cada fila contiene: código, nombre, stock actual y stock mínimo.
    inventario = [
        ["A001", "Teclado", 8, 15],
        ["A002", "Mouse", 20, 10],
        ["A003", "Monitor", 3, 8],
        ["A004", "Impresora", 5, 5],
        ["A005", "Disco SSD", 4, 12]
    ]

    mostrar_reabastecimiento(inventario)


if __name__ == "__main__":
    main()
