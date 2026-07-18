# ------------------------------------------------------------
# Nombre del estudiante: Esteban Daniel Arias Maya
# Programa: Ingeniería en Sistemas
# Grupo: 213022_107
# Código fuente: Autoría propia
# Fase 5 - Evaluación final POA
# ------------------------------------------------------------

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):

    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral:
        descuento = "Sí"
        precio_final = precio_base * 0.85
    else:
        descuento = "No"
        precio_final = precio_base

    return precio_final, descuento


# Matriz donde se almacenarán los productos
menu = []

print("=" * 80)
print("          PROMOCIÓN DEL MENÚ DEL RESTAURANTE")
print("=" * 80)

# Datos de la promoción
categoria_objetivo = input("\nIngrese la categoría que tendrá promoción: ")
umbral = float(input("Ingrese el precio mínimo para aplicar el descuento: "))

print("\nREGISTRO DE PRODUCTOS")

# Registro de los productos
for i in range(6):

    print(f"\nProducto {i + 1}")

    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio_base = float(input("Precio base: "))

    menu.append([nombre, categoria, precio_base])

print("\n" + "=" * 80)
print("RESULTADO DE LA PROMOCIÓN")
print("=" * 80)

print(f"\nCategoría con promoción: {categoria_objetivo}")
print(f"Precio mínimo para descuento: ${umbral:,.0f}")

print("\n{:<25} {:<15} {:>15} {:>12} {:>15}".format(
    "Producto",
    "Categoría",
    "Precio Base",
    "Descuento",
    "Precio Final"))

print("-" * 90)

# Mostrar resultados
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final, descuento = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    print("{:<25} {:<15} ${:>14,.0f} {:>12} ${:>14,.0f}".format(
        nombre,
        categoria,
        precio_base,
        descuento,
        precio_final
    ))
