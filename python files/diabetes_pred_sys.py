# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numpy as np



# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/diabetes_model.sav','rb'))

input_data = (10,139,80,0,0,27.1,1.441,57)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('This person is not a diabetic person.')
else:
  print('This person is a diabetic person.')