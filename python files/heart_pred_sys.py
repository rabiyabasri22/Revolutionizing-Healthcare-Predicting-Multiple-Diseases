# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:03:56 2024

@author: HP
"""

import pickle
import numpy as np

# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/heart_model.sav','rb'))


input_data = (44,1,0,112,290,0,0,153,0,0,2,1,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')