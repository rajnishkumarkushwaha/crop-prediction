# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:37:37 2022

@author: rajni
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('D:/machine learning/s_model.sav','rb'))

input_data = (209.0,1,0,1,0.0,0.0,0.0,2)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
    print("ALIVE")
else:
    print("DAMAGED DUE TO OTHER CAUSES")