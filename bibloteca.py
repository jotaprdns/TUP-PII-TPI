import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        cant_ej_pr = libro['cant_ej_pr']
    if cant_ej_pr > 0:
        print(f"Para el libro '{libro['titulo']}' hay {cant_ej_pr} ejemplares prestados.")

    if all(libro['cant_ej_pr'] == 0 for libro in libros):
        print("No hay ejemplares prestados.")
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
    #completar
    return None

def devolver_ejemplar_libro():
    #completar
    return None