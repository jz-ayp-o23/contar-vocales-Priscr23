"""
Diseña un programa para determinar el número de vocales en una frase.
"""
#Entradas
palabra = input("Introduzca una frase: ")
palabra = palabra.lower()

#Procesos
contador_vocales = 0
vocales = ['a', 'e', 'i', 'o', 'u']

for caracter in palabra:
    if caracter in vocales:
        contador_vocales += 1

# Salida
print(f"la frase tiene {contador_vocales} vocales")



