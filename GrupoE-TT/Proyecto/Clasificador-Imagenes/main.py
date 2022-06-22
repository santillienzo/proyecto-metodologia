from analizar import predecir
import os
import shutil

print("\n\n--- Metodologia de la Investigacion - (Desarrollado por: \n"
      "Enzo Leonel Sanchez, Enzo Santilli, Lucas Sanchez) ---\n\n")

# Verifica que exista la carpeta Imagenes
if not(os.path.exists('Imagenes')):
    print('No existe la carpeta Imagenes')
    exit(1)

# Si no existe la carpeta Gatos, la crea
if not(os.path.exists('./Imagenes/Gatos')):
    print('No existe la carpeta Gatos')
    os.mkdir('./Imagenes/Gatos')

if not(os.path.exists('./Imagenes/Perros')):
    print('No existe la carpeta Perros')
    os.mkdir('./Imagenes/Perros')

# Almacena en una lista, los nombres de todos los archivos que estan dentro de Imagenes
contenido = os.listdir('./Imagenes')

# Recorre toda la lista buscando archivos con formato de imagenes
for fichero in contenido:
    if os.path.isfile(os.path.join('./Imagenes', fichero)) and fichero.endswith(('.jpg','.jpeg','.png')):
        # Utiliza la funcion predecir del archivo analizar
        resultado = predecir(f'./Imagenes/{fichero}')
        if(resultado == 1):
            print(f'{fichero} --> :Gato')
            # Si el resultado es 1, mueve la imagen a la carpeta Gatos
            shutil.move(f'./Imagenes/{fichero}', './Imagenes/Gatos')
        elif(resultado == 2):
            print(f'{fichero} --> :Perro')
            # Si el resultado es 2, mueve la imagen a la carpeta Perros
            shutil.move(f'./Imagenes/{fichero}', './Imagenes/Perros')

