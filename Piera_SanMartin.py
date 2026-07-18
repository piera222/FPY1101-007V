
# DICCIONARIOS 


prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False]
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2]
}


# ======================
# VALIDACION
# ======================

def validar_codigo(codigo):
    return codigo.strip() != ""


def validar_texto(texto):
    return texto.strip() != ""


def validar_unisex(valor):
    return valor.lower() in ["s", "n"]


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0


# =========================
# OPCIÓN 1
# =========================

def unidades_categoria(categoria):
    total = 0

    for codigo, datos in prendas.items():
        if datos[1].lower() == categoria.lower():
            total += bodega[codigo][1]

    print(f"El total de unidades disponibles es: {total}")


# =========================
# OPCIoN 2
# ========================

def busqueda_precio(p_min, p_max):
    resultado = []

    for codigo, datos_bodega in bodega.items():

        precio = datos_bodega[0]
        unidades = datos_bodega[1]

        if p_min <= precio <= p_max and unidades > 0:
            nombre = prendas[codigo][0]
            resultado.append(f"{nombre}--{codigo}")

    resultado.sort()

    if len(resultado) == 0:
        print("No hay prendas en ese rango de precios.")
    else:
        print("Las prendas encontradas son:", resultado)

# =========================
# OPCIÓN 3
# =========================

def actualizar_precio(codigo, nuevo_precio):

    codigo = codigo.upper()

    if codigo not in bodega:
        return False

    bodega[codigo][0] = nuevo_precio
    return True


# =========================
# OPCIÓN 4
# =========================

def agregar_prenda(codigo, nombre, categoria,
                   talla, color, material,
                   es_unisex, precio, unidades):

    codigo = codigo.upper()

    if codigo in prendas:
        return False

    prendas[codigo] = [
        nombre,
        categoria,
        talla,
        color,
        material,
        es_unisex
    ]

    bodega[codigo] = [
        precio,
        unidades
    ]

    return True

# =====================
# OPCIÓN 5
# =====================

def eliminar_prenda(codigo):

    codigo = codigo.upper()

    if codigo not in prendas:
        return False

    del prendas[codigo]
    del bodega[codigo]

    return True

# =========================
# MENÚ PRINCIPAL
# =========================

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

    opcion = input("Ingrese opción: ")

    # OPCIÓN 1
    if opcion =="1":

        categoria = input("Ingrese categoría a consultar: ")
        unidades_categoria(categoria)

    # OPCIÓN 2
    elif opcion =="2":

        while True:

            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break

            except:
                print("Debe ingresar valores enteros")

        busqueda_precio(p_min, p_max)

    # OPCIÓN 3
    elif opcion == "3":
        while True:

            codigo = input("Ingrese código de la prenda: ")

            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))

                if nuevo_precio <= 0:
                    print("Precio inválido")
                    continue

            except:
                print("Debe ingresar un precio válido")
                continue

            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")

            respuesta = input(
                "¿Desea actualizar otro precio (s/n)?: "
            ).lower()

            if respuesta == "n":
                break
    # OPCIÓN 4
    elif opcion == "4":

        codigo = input("Ingrese código de la prenda: ")

        if not validar_codigo(codigo):
            print("Código inválido")
            continue

        nombre = input("Ingrese nombre: ")

        if not validar_texto(nombre):
            print("Nombre inválido")
            continue

        categoria = input("Ingrese categoría: ")

        if not validar_texto(categoria):
            print("Categoría inválida")
            continue

        talla = input("Ingrese talla: ")

        if not validar_texto(talla):
            print("Talla inválida")
            continue

        color = input("Ingrese color: ")

        if not validar_texto(color):
            print("Color inválido")
            continue

        material = input("Ingrese material: ")

        if not validar_texto(material):
            print("Material inválido")
            continue

        unisex = input("¿Es unisex? (s/n): ").lower()

        if not validar_unisex(unisex):
            print("Valor unisex inválido")
            continue

        try:
            precio = int(input("Ingrese precio: "))
        except:
            print("Precio inválido")
            continue

        if not validar_precio(precio):
            print("Precio inválido")
            continue

        try:
            unidades = int(input("Ingrese unidades: "))
        except:
            print("Unidades inválidas")
            continue

        if not validar_unidades(unidades):
            print("Unidades inválidas")
            continue

        es_unisex = unisex == "s"

        if agregar_prenda(
            codigo,
            nombre,
            categoria,
            talla,
            color,
            material,
            es_unisex,
            precio,
            unidades
        ):
            print("Prenda agregada")
        else:
            print("El código ya existe")

    # OPCIÓN 5
    elif opcion == "5":

        codigo = input(
            "Ingrese código de la prenda a eliminar: "
        )

        if eliminar_prenda(codigo):
            print("Prenda eliminada")
        else:
            print("El código no existe")

    # OPCIÓN 6
    elif opcion == "6":

        print("Programa finalizado.")
        break

    else:
        print("Debe seleccionar una opción válida")