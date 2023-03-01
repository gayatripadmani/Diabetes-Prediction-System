import pandas as pd
import numpy as np
import pickle
import streamlit as st


# Load the trained model
pickle_in = open('Automating_Diabetes_Prediction_System.pkl', 'rb')
knn = pickle.load(pickle_in)

#define the functions to pass an inputs

def prediction(Glucose, Insulin, BMI, Age):
    Glucose = Glucose
    Insulin = Insulin
    BMI = BMI
    Age = Age

    # Making a Prediction with new customer

    prediction = knn.predict(
        [[Glucose, Insulin, BMI, Age]])
    if prediction == 1:
        pred = "You have Diabetes, please consult a Doctor."
    elif prediction == 0:
        pred = "You don't have Diabetes."
    return pred

# let's create a function to define the web page

def main():
    # front end elements of the web page
    html_temp = """ 
        <div style ="background-color:blue; padding:15px"> 
        <h1 style ="color:black; text-align:center;">Automatic Diabetes Prediction System</h1> 
        </div> 
        """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    Glucose = st.number_input("Glucose Level")
    Insulin = st.number_input("Insulin")
    BMI = st.number_input("BMI")
    Age = st.number_input("Age")
    result = " "

    if st.button("Predict"):
        result = prediction(Glucose, Insulin, BMI, Age)
        st.success("{}".format(result))

if __name__=='__main__':
    main()
