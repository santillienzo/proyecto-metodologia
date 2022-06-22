def blancoYNegro(imagen_array):
    # Ciclo for que recorre alto de la imagen
    for alto in range(imagen_array.shape[0]):
        # Ciclo for que recorre ancho de la imagen
        for ancho in range(imagen_array.shape[1]):
            rojo = imagen_array[alto][ancho][0]
            verde = imagen_array[alto][ancho][1]
            azul = imagen_array[alto][ancho][2]
            gris = (int(rojo) + int(verde) + int(azul)) / 3
            # Ciclo for que recorre capas(colores) de la imagen
            for color in range(imagen_array.shape[2] - 1):
                # Reemplaza colores con promedio de los 3 colores
                imagen_array[alto][ancho][color] = gris
    return imagen_array


def convolucion(imagen_array):
    # Transforma cualquier array de imagen en blanco y negro primero
    imagen_array = blancoYNegro(imagen_array)
    nueva_imagen = imagen_array

    '''sobelVertical = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    sobelHorizontal = [[-1,-2,-1],[0,0,0],[1,2,1]]'''
    kernel = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    # El Ciclo recorre el alto(y) de la imagen pero comienza en 1 y termina 1 antes del total,
    # esto se debe a que el kernel también es una matriz y los bordes de la imagen pueden afectar el resultado
    for alto in range(1, imagen_array.shape[0] - 1):
        # El mismo ciclo que el anterior pero con el ancho(x) de la imagen
        for ancho in range(1, imagen_array.shape[1] - 1):
            totalY = 0
            totalX = 0
            total = 0

            # Ciclos para recorrer los kernel Sobel
            for kernelY in range(3):
                for kernelX in range(3):
                    '''totalY += sobelVertical[kernelY][kernelX] * imagen_array[alto+kernelY-1][ancho+kernelX-1][0]
                    totalX += sobelHorizontal[kernelY][kernelX] * imagen_array[alto+kernelY-1][ancho+kernelX-1][0]'''

                    total += kernel[kernelY][kernelX] * imagen_array[alto + kernelY - 1][ancho + kernelX - 1][0]

            nueva_imagen[alto][ancho][0] = total
            nueva_imagen[alto][ancho][1] = total
            nueva_imagen[alto][ancho][2] = total

    return nueva_imagen


def rojo(imagen_array):
    # Ciclo for que recorre alto de la imagen
    for alto in range(imagen_array.shape[0]):
        # Ciclo for que recorre ancho de la imagen
        for ancho in range(imagen_array.shape[1]):

            for color in range(1, imagen_array.shape[2] - 1):
                # Reemplaza colores con promedio de los 3 colores
                imagen_array[alto][ancho][color] = 0
    return imagen_array
