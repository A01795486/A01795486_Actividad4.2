"""
Programa 1: Caluclar las estadisticas descriptivas mediante un archivo elegido desde consola
"""

import time
import os
import sys

def calcular_estadisticas(numeros):
    """
    Función que calcula las estadísticas descriptivas:
    media, mediana, moda, varianza y desviación estándar
    """

    suma = sum(numeros)
    media = suma / len(numeros)


    numeros.sort()
    num_elementos = len(numeros)
    if num_elementos % 2 == 0:
        mediana = (numeros[num_elementos // 2 - 1] + numeros[num_elementos // 2]) / 2
    else:
        mediana = numeros[num_elementos // 2]


    frecuencias = {}
    for num in numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    moda = [k for k, v in frecuencias.items() if v == max(frecuencias.values())]


    suma_diferencias = sum((num - media) ** 2 for num in numeros)
    varianza = suma_diferencias / len(numeros)


    desviacion_estandar = varianza ** 0.5

    return media, mediana, moda, varianza, desviacion_estandar


def seleccionar_archivo():
    """
    Permite al usuario seleccionar un archivo para analizar.
    """
    archivos = [archivo for archivo in os.listdir() if
                archivo.endswith('.txt') and archivo != "A4.2.P1.Results-errata.txt"]

    print("Lista de archivos a analizar:")
    for i, archivo in enumerate(archivos):
        print(f"{i + 1}. {archivo}")

    seleccion = int(input("Indica el índice del archivo que quieres seleccionar: ")) - 1
    if seleccion < 0 or seleccion >= len(archivos):
        print("Selección no válida.")
        sys.exit()

    return archivos[seleccion]


def main():
    """
    Función principal que gestiona el flujo del programa:
    - Selección del archivo
    - Cálculo de estadísticas
    - Guardado y visualización de resultados
    """
    archivo = seleccionar_archivo()


    inicio = time.time()


    numeros = []
    with open(archivo, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numero = float(line.strip())
                numeros.append(numero)
            except ValueError:
                print(f"Error de dato no válido (se ignorará): {line.strip()}")

    if len(numeros) == 0:
        print("No hay datos válidos para procesar.")
        sys.exit()


    media, mediana, moda, varianza, desviacion_estandar = calcular_estadisticas(numeros)


    tiempo_final = time.time() - inicio


    resultados = f"""
    Archivo procesado: {archivo}
    Media: {media}
    Mediana: {mediana}
    Moda: {moda}
    Desviación Estándar: {desviacion_estandar}
    Varianza: {varianza}
    Tiempo de ejecución: {tiempo_final} segundos
    """


    print(resultados)


    with open("A4.2.P1.Results-errata.txt", 'w', encoding='utf-8') as file:
        file.write(resultados)


if __name__ == "__main__":
    main()
