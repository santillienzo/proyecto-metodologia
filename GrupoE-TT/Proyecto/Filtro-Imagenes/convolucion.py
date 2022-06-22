import numpy as np
import time
import matplotlib.pyplot as plt


class Kernel:
    # Objeto de tipo Kernel

    def __init__(self, matrix):
        self.__matrix = matrix
        self.__height = 0
        self.__width = 0

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def set_matrix(self, matrix):
        self.__matrix = matrix

    @property
    def height(self):
        return self.__matrix.shape[0]

    @height.setter
    def set_heigth(self, height):
        self.__height = height

    @property
    def width(self):
        return self.__matrix.shape[1]

    @width.setter
    def set_width(self, width):
        self.__width = width

def desenfoqueEstandar(imagen_array):
    start_time = time.time()
    nueva_imagen = imagen_array

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
            total = np.zeros(3, dtype='uint16')

            # Ciclos para recorrer los kernel Sobel
            for kernelY in range(3):
                for kernelX in range(3):
                    for color in range(3):
                        total[color] += kernel[kernelY][kernelX] * imagen_array[alto + kernelY - 1][ancho + kernelX - 1][color]

            for color in range(3):
                nueva_imagen[alto][ancho][color] = total[color] / 9

    print("--- Desenfoque ejecutado durante %.3f segundos ---" % (time.time() - start_time))

    return nueva_imagen


def convolution_2(i, j, imagen, kernel, borde):
    """ Realiza el producto de la imagen con el kernel, y suma sus resultados

    Retorna el pixel que resulta del producto

    Parametros:
    i: Posicion en el ancho
    j: Posicion en el alto
    imagen: Numpy Array de la imagen
    kernel : El kernel o filtro que se quiere aplicar
    borde: El borde a tener en cuenta cuando se aplica el filtro
    """
    return np.multiply(imagen[i - borde:i + borde + 1, j - borde:j + borde + 1],
                       kernel.matrix[:, :]).sum()


def aplicar_filtro(imagen, kernel):
    # APLICA UN FILTRO/KERNEL A UNA IMAGEN

    # Calcula el borde que debe agregarle a la imagen para aplicar el filtro
    border_size = int((kernel.height - 1) / 2)
    # Agrega el borde a la imagen
    bordered_image = np.pad(imagen, pad_width=border_size, mode='constant', constant_values=0)
    # Crea una matriz con el tamaño de la imagen y la rellena con 0
    result_image = np.zeros_like(imagen)
    # Crea el rango para recorrer la matriz
    horizontal_range = np.arange(border_size, bordered_image.shape[0] - border_size)
    vertical_range = np.arange(border_size, bordered_image.shape[1] - border_size)

    for i in horizontal_range:
        for j in vertical_range:
            result_image[i - border_size, j - border_size] = convolution_2(i, j, bordered_image, kernel, border_size)
    return result_image


def leer_imagen(archivo):
    # Lee una imagen y la convierte a Blanco y negro, retorna una matriz Numpy
    imagen = plt.imread(archivo)
    if imagen.ndim > 2:
        return np.dot(imagen[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        return imagen

def normalizar_imagen(imagen):
    valor_min = np.min(imagen)
    valor_max = np.max(imagen)
    return (imagen - valor_min) / (valor_max - valor_min)


def guardar_imagen(nombre, matriz):

    nuevo_archivo = "salida_" + nombre
    plt.imsave(f"{nuevo_archivo}", matriz, cmap="gray")
    print(f"-- Archivo: '{nuevo_archivo}' ¡generado exitosamente!.")


def mostrar_imagen(imagen, nombre):

    plt.figure(nombre)
    plt.imshow(imagen, cmap="gray")
    plt.xlabel("Ancho (px)")
    plt.ylabel("Alto (px)")
    plt.title(nombre)

def mostrar_graficos(): plt.show()

