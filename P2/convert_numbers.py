"""
Programa 2: convertir una lista de numeros a base hexadecimal y binario
"""
import os
import time


def decimal_a_binario(num):
    """
    Convierte un número entero en su formato binario.
    """
    binario = ""
    while num > 0:
        binario = str(num % 2) + binario
        num //= 2
    return binario if binario else "0"


def decimal_a_hexadecimal(num):
    """
    Convierte un número entero a su representación en sistema hexadecimal.
    """
    digitos_hex = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        hexadecimal = digitos_hex[num % 16] + hexadecimal
        num //= 16
    return hexadecimal if hexadecimal else "0"


def seleccionar_archivo():
    """
    Muestra los archivos disponibles y permite al usuario seleccionar uno.
    """
    archivos_txt = [f for f in os.listdir() if f.endswith('.txt') and f != "A4.2.P2.Results.txt"]
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


def procesar_datos(numeros):
    """
    Procesa los datos leyendo números y convirtiéndolos a binario y hexadecimal.
    """
    resultados = []
    for linea in numeros:
        try:
            num = int(linea.strip())
            binario = decimal_a_binario(num)
            hexadecimal = decimal_a_hexadecimal(num)
            resultado = f"Decimal: {num} | Binario: {binario} | Hexadecimal: {hexadecimal}"
            print(resultado)
            resultados.append(resultado)
        except ValueError:
            print(f"Datos inválidos: '{linea.strip()}' no es un elemento válido.")
    return resultados


def guardar_resultados(resultados):
    """
    Guarda los resultados en un archivo de salida.
    """
    archivo_resultados = "A4.2.P2.Results.txt"
    with open(archivo_resultados, 'w', encoding='utf-8') as archivo_salida:
        for resultado in resultados:
            archivo_salida.write(resultado + "\n")
    print(f"Resultados escritos en {archivo_resultados}")


def main():
    """
    Función principal donde se ejecutan las definiciones anteriores dependiendo del tipo de dato.
    """
    archivo_entrada = seleccionar_archivo()
    if archivo_entrada is None:
        return

    inicio_tiempo = time.time()

    numeros = leer_archivo(archivo_entrada)
    if numeros is None:
        return

    resultados = procesar_datos(numeros)

    tiempo_transcurrido = time.time() - inicio_tiempo
    resultados.append(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")

    guardar_resultados(resultados)

    print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")


if __name__ == "__main__":
    main()
