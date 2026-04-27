# Lista ordenada sin considerar tildes PC
import unicodedata

datos = ["Árbol", "Zebra", "Índice", "Avión", "Único", "Barco"]

def eliminar_tildes(cadena):
    # Normaliza a formato NFD (separa la letra del acento)
    forma_nfd = unicodedata.normalize('NFD', cadena)
    # Filtra y se queda solo con los caracteres que no sean acentos
    return "".join(c for c in forma_nfd if unicodedata.category(c) != 'Mn')

# Ordenar usando la funcion como clave (key)
datos_ordenados = sorted(datos, key=lambda x: eliminar_tildes(x).lower())

for elemento in datos_ordenados:
    print(elemento)
