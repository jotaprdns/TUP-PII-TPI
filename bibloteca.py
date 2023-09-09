import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print(f"Libro registrado con éxito. Código del libro: {nuevo_libro['cod']}")
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    buscar_codigo = input("Ingrese codigo del libro a prestar: ")
    for libro in libros:
        if buscar_codigo == libro["cod"]:
            autor = libro["autor"]
            titulo = libro["titulo"]
            disponibles = libro["cant_ej_ad"]
            print(f"Autor: {autor}")
            print(f"Titulo: {titulo}")
            print(f"Cantidad disponible: {disponibles}")
            if libro["cant_ej_ad"] == 0:
                print("No hay ejemplares disponibles para prestamo")
            else:
                libro["cant_ej_ad"] -= 1
                print(f"Actualizado el stock de libros con codigo {buscar_codigo}, por lo que existen una stock para prestar de: ")
                print(libro["cant_ej_ad"])
                libro["cant_ej_pr"] += 1
                print(f"El total de libros prestados con el codigo {buscar_codigo} es de: ")
                print(libro["cant_ej_pr"])
            return
    print(f"El codigo {buscar_codigo}, no se encuentra en la base de datos, verifique e intente nuevamente")
    
    return None

def devolver_ejemplar_libro():
    buscar_codigo = input("Ingrese codigo del libro a devolver: ")
    for libro in libros:
        if buscar_codigo == libro["cod"]:
            if libro["cant_ej_pr"] == 0:
                print("No hay registros de que se presto este libro, ingrese codigo nuevamente")
            else:
                libro["cant_ej_pr"] -= 1
                print(f"Actualizado el stock de libros con codigo {buscar_codigo}, por lo que existen una stock libros prestados de: ")
                print(libro["cant_ej_pr"])
                libro["cant_ej_ad"] += 1
                print(f"El total de libros disponibles para prestamo con el codigo {buscar_codigo} es de: ")
                print(libro["cant_ej_ad"])
            return
    print(f"El codigo {buscar_codigo}, no se encuentra en la base de datos, verifique e intente nuevamente")
    
    return None