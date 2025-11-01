# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:20:46 2024

@author: HP
"""

import pickle
import numpy as np

# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/lung_model.sav','rb'))

input_data =(68,2,1,2,1,1,2,1,1,1,1,1,1,1,)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#std_data=scaler.transform(input_data_reshaped)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person doesnot have Lung Cancer')
else:
  print('The Person have Lung Cancer')