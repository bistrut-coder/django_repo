import numpy as np 
import pandas as pd
import pickle
import streamlit as st

model = pickle.load(open(r'D:\task\home_pred.pkl',"rb"))

st.title("House Prediction model")

st.write("This model is using for house prediction according required area")

required_space = st.number_input("Enter required space", min_value=1.0,max_value=400.0,step=4.0)

if st.button("predict House Price"):
    space  = np.array([[required_space]])
    prediction = model.predict(space)
    st.success(f"For {required_space} the price is : {prediction[0]:,.2f}")

st.write("Thanx using our model")