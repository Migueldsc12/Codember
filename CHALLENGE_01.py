def contar_palabras(mensaje):
    palabras = mensaje.lower().split()

    recuento = {}

    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1

    resultado = ""
    for palabra, frecuencia in recuento.items():
        resultado += f"{palabra}{frecuencia}"

    return resultado