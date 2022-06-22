import time
import os.path
import convolucion as conv
import numpy as np

start_time = time.time()

filtro_laplace = conv.Kernel(np.matrix([[0, 1, 0],
                                         [1, -4, 1],
                                         [0, 1, 0]]))

filtro_gaussiano = conv.Kernel(np.matrix([[1, 4, 6, 4, 1],
                                    [4, 16, 24, 16, 4],
                                    [6, 24, 36, 24, 6],
                                    [4, 16, 24, 16, 4],
                                    [1, 4, 6, 4, 1]]) * 1 / 256)

filtro_detector_borde = conv.Kernel(np.matrix([[1, 2, 0, -2, -1],
                                          [1, 2, 0, -2, -1],
                                          [1, 2, 0, -2, -1],
                                          [1, 2, 0, -2, -1],
                                          [1, 2, 0, -2, -1]]))

print("--- Metodologia de la Investigacion - (Desarrollado por: \n"
      "Enzo Leonel Sanchez, Enzo Santilli, Lucas Sanchez) ---\n")
# Se ingresa el nombre de la imagen a procesar
archivo = input("Escriba el nombre del archivo de imagen a procesar: ")
print()
# Verifica que la imagen exista
if os.path.exists(archivo):
    # Se lee la imagen
    imagen_ref = conv.leer_imagen(archivo)

    # Se almacena el tiempo de comienzo del programa
    current_time = time.time()
    print("Iniciando convolucion con Filtro Laplaciano")

    # Se aplica filtro a la imagen
    laplacian_imagen = conv.aplicar_filtro(imagen_ref, filtro_laplace)
    print(f"-- Convolución usando Filtro Laplaciano terminada en {format((time.time() - current_time), '.3f')} segundos. --\n")
    imagen_laplace_normalizada = conv.normalizar_imagen(laplacian_imagen)

    print("- Guardando los resultados obtenidos.")
    conv.guardar_imagen("filtro_laplaciano_" + archivo, imagen_laplace_normalizada)

    current_time = time.time()
    print("Iniciando convolucion con Filtro Gaussiano")

    # Se aplica filtro a la imagen
    gaussiano_imagen = conv.aplicar_filtro(imagen_ref, filtro_gaussiano)
    print(
        f"-- Convolución usando Filtro Gaussiano terminada en {format((time.time() - current_time), '.3f')} segundos. --\n")
    imagen_gaussiano_normalizada = conv.normalizar_imagen(gaussiano_imagen)

    print("- Guardando los resultados obtenidos.")
    conv.guardar_imagen("filtro_gaussiano_" + archivo, imagen_gaussiano_normalizada)

    current_time = time.time()
    print("Iniciando convolucion con Filtro Detector Bordes")

    # Se aplica filtro a la imagen
    bordes_imagen = conv.aplicar_filtro(imagen_ref, filtro_detector_borde)
    print(
        f"-- Convolución usando Filtro Detector Borde terminada en {format((time.time() - current_time), '.3f')} segundos. --\n")
    imagen_bordes_normalizada = conv.normalizar_imagen(bordes_imagen)

    print("- Guardando los resultados obtenidos.")
    conv.guardar_imagen("filtro_bordes_" + archivo, imagen_bordes_normalizada)
    print("\n")

    print("\n- Generando gráficos de las imagenes resultantes...")
    conv.mostrar_imagen(imagen_ref, f"Imagen Original {archivo}")
    conv.mostrar_imagen(imagen_laplace_normalizada, f"Filtro 'Laplaciano' aplicado en {archivo}")
    conv.mostrar_imagen(imagen_gaussiano_normalizada, f"Filtro 'Suavizado Gaussiano' aplicado en {archivo}")
    conv.mostrar_imagen(imagen_bordes_normalizada, f"Filtro 'Detector de Bordes' aplicado en {archivo}")
    conv.mostrar_graficos()
else:
    print("No existe ubicacion de archivo")
