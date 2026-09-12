"""Programa para calcular el total de una compra en una tienda."""


def calcular_total(precio, cantidad):
    """Calcula y devuelve el total que debe pagar el cliente."""
    total = precio * cantidad
    return total


if __name__ == "__main__":
    print("CÁLCULO DEL TOTAL DE UNA COMPRA")

    precio_producto = float(input("Ingrese el precio del producto: $"))
    cantidad_productos = int(input("Ingrese la cantidad de productos: "))

    resultado = calcular_total(precio_producto, cantidad_productos)

    print(f"El total de la compra es: ${resultado:.2f}")