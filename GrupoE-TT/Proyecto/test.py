import numpy as np
import colores as col
from PIL import Image
import convolucion as conv

original = Image.open('imagenes/cat.jpg')
similar = Image.open('imagenes/catCopia.jpg')
if not np.array_equal(original.size,similar.size):
    similar = similar.resize(original.size)

original_array = np.asarray(original)
similar_array = np.asarray(similar)

print(col.porcentajeSimilar(original_array,similar_array,5))

'''original_array = np.asarray(original)
similar_array = np.asarray(similar)

Image.fromarray(conv.desenfoqueEstandar(original_array)).save("asdasdasads.jpg")'''

print("Programa Terminado")
