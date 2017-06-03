import numpy as np
import cv2
from keras.models import load_model
from keras.models import Model
from keras.preprocessing import image
from PIL import Image
from keras import backend as K


imgs = Image.open( r'C:\Users\TheJonasLegend\Desktop\Data\Img\Sample012\img012-009.png')
imgs.load()    
imgs = np.array(imgs)
imgs = cv2.resize(imgs, (28,28))
#imgs = cv2.cvtColor(imgs, cv2.COLOR_GRAY2BGR) 
imgs = np.reshape(imgs, (-1, 28,28,3) )
#imgs= np.expand_dims(imgs, axis=0)

model_1 = load_model('modelo1.h5')

#model_1.evaluate_generator(validation_generator, steps = 15)

prediction = model_1.predict(imgs)
print(prediction)
if prediction == 0.:
    print("Letra A")
    
if prediction == 1.:
    print("Letra B")