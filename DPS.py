# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:41:47 2023

@author: awast
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved mode
loaded_model=pickle.load(open('trained_model.sav','rb'))


#creating function for prediction
def diabetes_predict(input_data):
    input_arr=np.array(input_data,dtype=np.float64)
    input_arr_r=input_arr.reshape(1,-1)
    predict=loaded_model.predict(input_arr_r)
    if predict[0]==0 :
       return 'Diabetes Not Detected'
    else :
       return 'Diabetes Detected' 
    
    
def main():
    
    #Giving title
    st.title('Diabetes Prediction System')
    
    #Getting user input
    pr=st.text_input('Pregnancies')
    G=st.text_input('Glucose')
    bp=st.text_input('BloodPressure')
    sth=st.text_input('Skin Thickness')
    ins=st.text_input('Insulin')
    bmi=st.text_input('BMI')
    pdf=st.text_input('Diabetes Pedigree Function')
    age=st.text_input('Age')
        
    predict=''
    
    if st.button("Predict Diabetes"):
        predict=diabetes_predict([pr,G,bp,sth,ins,bmi,pdf,age])
        
    
    st.success(predict)
    
    
    
    
    
if __name__ == '__main__':
    main()










    
