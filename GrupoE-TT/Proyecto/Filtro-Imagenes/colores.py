import numpy as np


# Se ultiliza para saber cuantas veces aparece un color en una imagen
def histograma(imagen_array):
    colores = np.zeros([3, 256], dtype=int)

    for alto in range(imagen_array.shape[0]):
        for ancho in range(imagen_array.shape[1]):
            for color in range(3):
                colores[color][imagen_array[alto][ancho][color]] += 1
    return colores


def compararPixeles(imagen_uno, imagen_dos, holgura):
    pixeles_similares = np.zeros([imagen_uno.shape[0], imagen_uno.shape[1]], dtype=bool)

    for alto in range(imagen_uno.shape[0]):
        for ancho in range(imagen_uno.shape[1]):
            parecido = np.zeros(3, dtype=bool)
            for color in range(3):
                if imagen_dos[alto][ancho][color] >= imagen_uno[alto][ancho][color] - holgura and \
                        imagen_uno[alto][ancho][color] <= imagen_uno[alto][ancho][color] + holgura:
                    parecido[color] = True
            pixeles_similares[alto][ancho] = parecido[0] and parecido[1] and parecido[2]
    return pixeles_similares

def porcentajeSimilar(imagen_uno, imagen_dos, holgura):
    pixeles_similares = compararPixeles(imagen_uno,imagen_dos,holgura)
    cantidadSimilares = 0

    total_pixeles = imagen_uno.shape[0] * imagen_uno.shape[1]

    for alto in range(pixeles_similares.shape[0]):
        for ancho in range(pixeles_similares.shape[1]):
            if pixeles_similares[alto][ancho] == True:
                cantidadSimilares += 1
    porcentaje = (cantidadSimilares*100)/total_pixeles
    return porcentaje
