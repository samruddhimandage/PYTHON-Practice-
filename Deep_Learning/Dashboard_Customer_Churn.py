import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Marvellous Infosystems Dashboard")

st.title("Marvellous Infosystems By Piyush Manohar Khairnar")
st.header("Customer Churn Prediction")
st.write("Machine Leanring Application Dashboard")

model = joblib.load("Marvellous_ML_Customer_Churn.pkl")

st.subheader("Enter customer details")

age = st.number_input("Customer Age",min_value=1)
tenure = st.number_input("Tenure (Months)",min_value=0)
charges = st.number_input("Monthly Charges",min_value=0)
calls = st.number_input("Support calls",min_value=0)

if st.button("Predict Churn"):
    new_customer = pd.DataFrame({
    "Age" : [age],
    "Tenure" : [tenure],
    "MonthlyCharges" : [charges],
    "SupportCalls" : [calls]
    })

    prediction = model.predict(new_customer)[0]

    if prediction == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is unlikely to churn")

st.divider()

st.caption("Marvellous Infosystems Dashbord")