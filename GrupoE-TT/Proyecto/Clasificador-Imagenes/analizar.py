import numpy as np
from keras.utils import CustomObjectScope
from keras.models import load_model
from tensorflow.python.ops.init_ops_v2 import glorot_uniform
import matplotlib.pyplot as plt
import cv2

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    TAMANO_IMG = 100
    modelo = './modelo/modelo.h5'
    pesos_modelo = './modelo/pesos.h5'
    cnn = load_model(modelo)
    cnn.load_weights(pesos_modelo)

    def predecir(archivo):
        imagen = plt.imread(archivo)
        imagen = cv2.resize(imagen, (TAMANO_IMG, TAMANO_IMG))
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen = imagen.reshape(1, TAMANO_IMG, TAMANO_IMG, 1)
        x = np.array(imagen).astype(float) / 255
        array = cnn.predict(x)
        result = array[0]
        print(result)
        if result <= .5:
            # Es Gato
            return 1
        else:
            # Es Perro
            return 2