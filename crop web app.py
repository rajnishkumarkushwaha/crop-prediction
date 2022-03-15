# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:42:41 2022

@author: rajni
"""

import numpy as np 
import pickle 
import streamlit as st

loaded_model = pickle.load(open('D:/machine learning/s_model.sav','rb')) 

def crop_prediction(input_data):
   
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
    print(prediction)
    
    if (prediction[0]== 0):
        return "ALIVE"
    else:
        return "DAMAGED DUE TO OTHER CAUSES"
    
def main():
        
    st.title('CROP PREDICTION')
        
        
    Estimated  = st.text_input('Number of insects')
    Crop       = st.text_input('Crop_Type')
    Soil       = st.text_input('Soil_Type')
    Pesticide  = st.text_input('Pesticide_Use_Category')
    Doses      = st.text_input('Number_Doses_Week')
    Used       = st.text_input('Number_Weeks_Used')
    Quit       = st.text_input("Number__Weeks_Quit")
    Season     = st.text_input('Season')
           
    crop =' '
           
    if st.button('crop test result'):
        crop = crop_prediction([Estimated,Crop,Soil,Pesticide,Doses,Used,Quit,Season])
            
    st.success(crop)
           
           
if __name__ == '__main__':
    main()
            