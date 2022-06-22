# Procesador de Imagenes con Filtros
Este es un proyecto de código abierto para el desarrollo de un software que detecte y aplique filtros de distinto tipos a un grupo de imágenes. Pretende usarse para poder agrupar imágenes similares.

## Introducción
Actualmente, existen programas que ofrecen la búsqueda de archivos repetidos, pero únicamente realizan la búsqueda por su tamaño o nombre, y no por el contenido de las imágenes.

La propuesta de este proyecto consiste en la búsqueda de imágenes similares de la forma más cercana a lo que una persona lo haría, basándose en sus colores, figuras y tamaños.

## Librerias necesarias
- La libreria Os-Path
- La biblioteca numpy
- La biblioteca matplotlib
- La libreria keras
- La libreria tensorflow
- La libreria OpenCv

## Instalación

Se comienza con la instalación del gestor de paquetes PIP de Python. Para instalarlo, ejecutar en la terminal:

```bash
sudo apt install python3-pip
```

Desde la terminal del sistema Operativo, y con el gestor de paquetes PIP de Python, ejecutar:

```bash
pip install numpy
pip install matplotlib
pip install time
pip install keras
pip install tensorflow
pip install opencv-python
```

## Ejecucion
Para ejecutar el programa debe ubicarse en la carpeta del programa y ejecutar desde la terminal:
```bash
sudo python3 main.py
```
En algunos casos, el comando podría ser distinto:
```bash
sudo python main.py
```

En el caso del Filtro de Imagenes, el programa pedirá que ingrese el nombre de la imagen a procesar. Colocar la imagen en el directorio del programa. Al terminar de procesar la imagen, mostrará ventanas con los distintos tipos de Convoluciones. Con esto se puede entender el principio de funcionamiento de las Inteligencias Artificiales Convolucionales.

Si se ejecuta el Clasificador de Imágenes, el programa comprueba que exista la carpeta "Imagenes" en el directorio, de no existir, el programa se cierra.
Se debe colocar dentro de la carpeta Imagenes, todos los archivos que se quieran clasificar y el programa creará automáticamente las carpetas con las categorias.

Actualmente, el programa clasifica imagenes que contengan gatos o perros, solamente con formato .jpg, .jpeg, o .png. Se dejó imagenes de prueba dentro de la carpeta Imagenes para comprobar el funcionamiento. Al ejecutarse, creará automáticamente dos carpetas, Gatos y Perros, y colocará dentro las imagenes que les corresponda.


