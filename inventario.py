def mostrar_menu():
    print("\nBienvenido al sistema de inventario de la tienda.")
    print("1. Agregar un producto al inventario")
    print("2. Vender un producto")
    print("3. Mostrar inventario")
    print("4. Salir")

def agregar_producto(inventario):
    nombre_producto = input("Ingresa el nombre del producto: ").capitalize()
    cantidad = int(input(f"Ingresa la cantidad de {nombre_producto}: "))
    
    if nombre_producto in inventario:
        inventario[nombre_producto] += cantidad
    else:
        inventario[nombre_producto] = cantidad
    
    print(f"Producto agregado al inventario. {nombre_producto}: {inventario[nombre_producto]} unidades.")

def vender_producto(inventario):
    nombre_producto = input("Ingresa el nombre del producto a vender: ").capitalize()
    if nombre_producto in inventario:
        cantidad = int(input(f"Ingresa la cantidad a vender de {nombre_producto}: "))
        if cantidad <= inventario[nombre_producto]:
            inventario[nombre_producto] -= cantidad
            print("Venta realizada.")
        else:
            print("No hay suficiente stock.")
    else:
        print("El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    print("\nInventario:")
    if inventario:
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad}")
    else:
        print("El inventario está vacío.")

def main():
    inventario = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            vender_producto(inventario)
        elif opcion == '3':
            mostrar_inventario(inventario)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()