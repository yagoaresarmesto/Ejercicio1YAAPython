from io import open
import os
import shutil


def escribir_menu():
    print('\nFICHEROS\n1. Leer fichero de texto\n2. Copiar fichero\n3. Listar archivos de directorio\n0. Salir')


def pedir_opcion():
    print('Escoja una opción: ', end='')


def leer_opcion():
    try:
        op = int(input())
    except ValueError:
        op = None
    finally:
        return op


def leer_fichero():
    ruta = input("Escribe el directorio del archivo de texto: ")  # Pedimos la ruta por consola

    if (os.path.exists(ruta)):
        text_file = open(ruta, "r")  # La abrimos
        texto = text_file.read()  # Leemos el txt
        text_file.close()  # Cerramos el txt
        print(texto)  # Imprimimos por consola el contenido
    else:
        print(
            "Ruta incorrecta: [" + ruta + "], comprueba si es una ruta existente o si la ruta corresponde a un fichero de texto.")


def copiar_fichero():
    rutaOrigen = input("Escribe la ruta de tu archivo de texto que quiera copiar: ")
    rutaCopiar = input("Escribe la ruta donde la quiera pegar: ")
    if (os.path.exists(rutaOrigen) and os.path.exists(rutaCopiar)):
        shutil.copy(rutaOrigen, rutaCopiar)
        print("Copiado con éxito")
    else:
        print(
            "Ruta/s incorrecta/s: [" + rutaOrigen + "]" + "[" + rutaCopiar + "] , comprueba si algunas de estas rutas son existentes.")


def listar_directorio():
    ruta = input("Escribe el directorio a listar: ")  # Pedimos la ruta por consola
    fun = lambda x: os.path.isfile(os.path.join(ruta, x))
    files_list = filter(fun, os.listdir(ruta))

    size_of_file = [
        (f, os.stat(os.path.join(ruta, f)).st_size)
        for f in files_list
    ]

    fun = lambda x: x[1]
    for f, s in sorted(size_of_file, key=fun):
        print(
            "{} : {}bk".format(os.path.join(ruta, f), round(s / 1000, 3)))  # Hacemos la conversión de bytes a kilobytes


if __name__ == '__main__':
    while True:
        escribir_menu()
        pedir_opcion()
        opcion = leer_opcion()
        if opcion == 0:
            exit(0)
        elif opcion == 1:
            leer_fichero()
        elif opcion == 2:
            copiar_fichero()
        elif opcion == 3:
            listar_directorio()
        else:
            print('Opción no válida, elige una opción válida')
