# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:59:39 2024

@author: HP
"""

import pickle
import numpy as np

# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/parkinsons_model.sav','rb'))

input_data = (243.43900,250.91200,232.43500,0.00210,0.000009,0.00109,0.00137,0.00327,0.01419,0.12600,0.00777,0.00898,0.01033,0.02330,0.00454,25.36800,0.438296,0.635285,-7.057869,0.091608,2.330716,0.091470)
# changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons Disease")

