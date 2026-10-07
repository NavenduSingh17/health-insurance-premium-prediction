#---------------------------------------------------------------------------------------------------------
# Author : NAVENDU SINGH
#---------------------------------------------------------------------------------------------------------

import streamlit as st
from prediction_helper import predict

#st.title('HEALTH INSURANCE PREMIUM PREDICTOR')
st.markdown("### HEALTH INSURANCE PREMIUM PREDICTOR")
st.write("")
st.write("")

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Underweight', 'Normal', 'Overweight', 'Obesity'],
    'Smoking Status': ['No Smoking', 'Occasional', 'Regular'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold'],
    'Heart Disease': ['Yes', 'No'],
    'Diabetes': ['Yes', 'No'],
    'High Blood Pressure': ['Yes', 'No'],
    'Thyroid': ['Yes', 'No']
}

row1 = st.columns(4)
row2 = st.columns(4)
row3 = st.columns(4)
row4 = st.columns(4)
st.write("")
st.write("")
st.write("")

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=25)
with row1[1]:
    gender = st.selectbox('Gender', categorical_options['Gender']) 
with row1[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
with row1[3]:
    income_lakhs = st.number_input('Annual Income (Lakhs)', step=1, min_value=0, max_value=200, value=10)

with row2[0]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row2[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row2[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'], index=1)
with row2[3]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])

with row3[0]:
    health_heart_disease = st.selectbox('Heart Disease', categorical_options['Heart Disease'], index=1)
with row3[1]:
    health_diabetes = st.selectbox('Diabetes', categorical_options['Diabetes'], index=1)
with row3[2]:
    health_high_bp = st.selectbox('High Blood Pressure', categorical_options['High Blood Pressure'], index=1)
with row3[3]:
    health_thyroid = st.selectbox('Thyroid', categorical_options['Thyroid'], index=1)

with row4[0]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row4[2]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Gender': gender,
    'Employment Status': employment_status,
    'Annual Income (Lakhs)': income_lakhs,
    'Marital Status': marital_status,
    'Number of Dependants': number_of_dependants,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Insurance Plan': insurance_plan,
    'Genetical Risk': genetical_risk,
    'Heart Disease': health_heart_disease,
    'Diabetes': health_diabetes,
    'High Blood Pressure': health_high_bp,
    'Thyroid': health_thyroid
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Cost for Health Insurance Annual Premium : ₹ {prediction}')
