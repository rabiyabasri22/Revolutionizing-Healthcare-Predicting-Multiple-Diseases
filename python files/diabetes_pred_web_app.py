# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:03:40 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/diabetes_model.sav','rb'))

# Creating a function for Prediction
def diabetes_pred(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = load_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'This person is not a diabetic person.'
    else:
      return 'This person is a diabetic person.'
  
def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')  
    
    # getting the input data from the user
       
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diabetes_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diabetes_diagnosis = diabetes_pred([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diabetes_diagnosis)
    
    
if __name__ == '__main__':
    main()