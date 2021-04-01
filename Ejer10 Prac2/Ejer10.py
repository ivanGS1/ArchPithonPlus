cadena=input('Ingrese una palabra y se calculara el valor de la misma ').upper()
diccionario = {
    ('A','E','I','O','U','L','N','R','S','T'):1,
    ('D','G'):2,
    ('B','C','M','P'):3,
    ('F','H','V','W','Y'):4,
    ('K'):5,
    ('J','X'):8,
    ('Q','Z'):10
}

def valores(cadena,diccionario):
    cant=0
    for p in cadena:
        for clave in diccionario:
            for item in clave:
                if p in item:
                    cant=cant+diccionario[clave]
    return cant

print(valores(cadena,diccionario))