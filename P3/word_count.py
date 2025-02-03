"""
Problema 3: Programa para contar las palabras y sus frecuencias en un archivo.
"""
import os
import time


def contar_palabras(archivo_entrada):
    """
    Cuenta las palabras y su frecuencia en el archivo proporcionado.
    """
    frecuencias = {}
    for linea in archivo_entrada:
        palabras = linea.strip().split()
        for palabra in palabras:
            palabra = palabra.lower()
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
    return frecuencias


def seleccionar_archivo():
    """
    Muestra los archivos disponibles y permite al usuario seleccionar uno.
    """
    archivos_txt = [f for f in os.listdir() if f.endswith('.txt')
                    and not f.endswith('.Results.txt')]
    print("Lista de archivos a analizar:")
    for idx, archivo in enumerate(archivos_txt):
        print(f"{idx + 1}. {archivo}")

    try:
        seleccion = int(input("Indica el índice del archivo que quieres seleccionar: "))
        return archivos_txt[seleccion - 1]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return None


def leer_archivo(archivo_entrada):
    """
    Lee el contenido del archivo seleccionado.
    """
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        return None


def guardar_resultados(frecuencias, archivo_salida):
    """
    Guarda las frecuencias de las palabras en un archivo de salida.
    """
    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        for palabra, frecuencia in sorted(frecuencias.items()):
            archivo.write(f"{palabra}: {frecuencia}\n")
    print(f"Resultados escritos en {archivo_salida}")


def main():
    """
    Función principal donde se ejecutan las definiciones anteriores dependiendo del tipo de dato.
    """
    archivo_entrada = seleccionar_archivo()
    if archivo_entrada is None:
        return

    inicio_tiempo = time.time()

    lineas = leer_archivo(archivo_entrada)
    if lineas is None:
        return

    frecuencias = contar_palabras(lineas)

    tiempo_transcurrido = time.time() - inicio_tiempo


    archivo_resultados = archivo_entrada.replace(".txt", ".Results.txt")

    guardar_resultados(frecuencias, archivo_resultados)

    print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")


if __name__ == "__main__":
    main()
