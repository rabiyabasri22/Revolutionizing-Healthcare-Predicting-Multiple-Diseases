# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:22:17 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# Loading the saved Model
load_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/lung_model.sav','rb'))

# Creating a function for Prediction
def lung_pred(input_data):

    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    #std_data=scaler.transform(input_data_reshaped)

    prediction = load_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person doesnot have Lung Cancer'
    else:
      return 'The Person have Lung Cancer'

  
def main():
    
    # giving a title
    st.title('Lung Cancer Prediction Web App')  
    
    # getting the input data from the user
    age = st.text_input('Age')
    smoking = st.text_input('Smoking')
    yellow_fingers = st.text_input('Yellow Fingers')
    anxiety = st.text_input('Anxiety')
    peer_pressure = st.text_input('Peer presure')
    chronic_disease = st.text_input('Chronic Disease')
    fatigue = st.text_input('Fatigue')
    allergy = st.text_input('Allergy')
    wheezing = st.text_input('Wheezing')
    alcohol_consuming = st.text_input('Alchohol Consuming')
    coughing = st.text_input('Coughing')
    shortness_of_breath = st.text_input('Shortness of Breath')
    swallowing_difficulty = st.text_input('Swallowing Difficulty')
    chest_pain = st.text_input('Chest Pain')

        
    # code for Prediction
    lung_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Lung Cancer Prediction Test Result'):
        lung_diagnosis = lung_pred([age,smoking,yellow_fingers,anxiety,peer_pressure,chronic_disease,fatigue,allergy,wheezing,alcohol_consuming,coughing,shortness_of_breath,swallowing_difficulty,chest_pain])                       
        
    st.success(lung_diagnosis)
    
    
    
if __name__ == '__main__':
    main()