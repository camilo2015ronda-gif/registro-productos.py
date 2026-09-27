def mostrar_productos(productos):
    print("\n--- PRODUCTOS REGISTRADOS ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")


def main():
    productos = []

    while True:
        print("\n===== REGISTRO DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            productos.append(producto)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            mostrar_productos(productos)

        elif opcion == "3":
            producto = input("Ingrese el producto que desea buscar: ")

            if producto in productos:
                print("El producto sí está registrado.")
            else:
                print("El producto no está registrado.")

        elif opcion == "4":
            producto = input("Ingrese el producto que desea eliminar: ")

            if producto in productos:
                productos.remove(producto)
                print("Producto eliminado correctamente.")
            else:
                print("El producto no está registrado.")

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()