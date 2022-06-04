import numpy as np
import colores as col
from PIL import Image
import transfor as tr

cat = Image.open('cat.jpg')
cat_array = np.asarray(cat)
panda = Image.open('catCopia.jpg')
panda_array = np.asarray(panda)

'''cat_filtro = tr.convolucion(cat_array)

print(cat_filtro[1][1])

Image.fromarray(cat_filtro).save("catPython.jpg")
print("Programa terminado")'''


print(col.porcentajeSimilar(cat_array,panda_array,5))
