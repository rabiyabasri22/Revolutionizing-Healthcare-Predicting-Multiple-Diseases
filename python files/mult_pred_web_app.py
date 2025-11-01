# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:48:27 2024

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('D:/Project/SourceCode/SAVfiles/diabetes_model.sav','rb'))

parkinsons_model = pickle.load(open('D:/Project/SourceCode/SAVfiles/parkinsons_model.sav','rb'))

heart_model = pickle.load(open('D:/Project/SourceCode/SAVfiles/heart_model.sav','rb'))

lung_model=pickle.load(open('D:/Project/SourceCode/SAVfiles/lung_model.sav','rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Home Page','Heart Disease Prediction',
                           'Lung Cancer Prediction',
                           'Diabetes Prediction',
                           'Parkinsons Prediction'],
                          icons=['house','heart','lungs','activity','person'],
                          default_index=0)

#Home Page
if(selected == 'Home Page'):
    st.title('Revolutionizing Healthcare : Machine Learning’s Precision in Predicting Multiple Diseases')
    st.markdown('A comprehensive project has been developed to predict various diseases, including diabetes, heart disease, lung cancer, and Parkinsons disease,utilizing the Random Forest algorithm.')    
    st.markdown('The integration of machine learning in healthcare has become indispensable, given the abundance of patient data available today.')
    st.markdown('Users can select from four disease options: heart disease, diabetes,Parkinsons disease, and lung cancer. This predictive system enables simultaneous detection of multiple diseases based on inputted health parameters, empowering individuals to monitor their well-being effectively.') 
    st.markdown('It serves as a proactive toolfor users to take preventive measures, leveraging predictive insights derived from machine learning algorithms. As technology continues to evolve, there is immense potentialto expand the system''s capabilities to include more diseases, thus enhancing its utility in healthcare monitoring and preventive healthcare measures.')
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
#Lung Cancer Prediction Page
if (selected == 'Lung Cancer Prediction'):
    
    # page title
    st.title('Lung Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        smoking = st.text_input('Smoking')
        
    with col3:
        yellow_fingers = st.text_input('Yellow Fingers')
        
    with col1:
        anxiety = st.text_input('Anxiety')
        
    with col2:
        peer_pressure = st.text_input('Peer presure')
        
    with col3:
        chronic_disease = st.text_input('Chronic Disease')
        
    with col1:
        fatigue = st.text_input('Fatigue')
        
    with col2:
        allergy = st.text_input('Allergy')
        
    with col3:
        wheezing = st.text_input('Wheezing')
        
    with col1:
        alcohol_consuming = st.text_input('Alchohol Consuming')
        
    with col2:
        coughing = st.text_input('Coughing')
        
    with col3:
        shortness_of_breath = st.text_input('Shortness of Breath')
        
    with col1:
        swallowing_difficulty = st.text_input('Swallowing Difficulty')
    
    with col2:
        chest_pain = st.text_input('Chest Pain')

        
        
     
     
    # code for Prediction
    lung_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Lung Cancer Prediction Test Result'):
        
        lung_prediction = lung_model.predict([[age,smoking,yellow_fingers,anxiety,peer_pressure,chronic_disease,fatigue,allergy,wheezing,alcohol_consuming,coughing,shortness_of_breath,swallowing_difficulty,chest_pain]])                          
        
        if (lung_prediction[0] == 1):
          lung_diagnosis = 'The person is having Lung Cancer'
        else:
          lung_diagnosis = 'The person does not have Lung cancer'
        
    st.success(lung_diagnosis)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)