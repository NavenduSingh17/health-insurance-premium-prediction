#---------------------------------------------------------------------------------------------------------
# Author : NAVENDU SINGH
#---------------------------------------------------------------------------------------------------------

import pandas as pd
import joblib

model_young = joblib.load("artifacts/young_population_model.joblib")
model_old = joblib.load("artifacts/old_population_model.joblib")

def calculate_health_risk_score(input_dict):
    score = 0
    if input_dict['Heart Disease'] == 'Yes':
        score = score + 8
    if input_dict['Diabetes'] == 'Yes':
        score = score + 6
    if input_dict['High Blood Pressure'] == 'Yes':
        score = score + 6
    if input_dict['Thyroid'] == 'Yes':
        score = score + 5
    return score

def preprocess_young(input_dict):
    health_risk_score = calculate_health_risk_score(input_dict)
    data = {
        'age': [input_dict['Age']],
        'gender': [input_dict['Gender']],
        'employment_status': [input_dict['Employment Status']],
        'income_lakhs': [input_dict['Annual Income (Lakhs)']],
        'marital_status': [input_dict['Marital Status']],
        'number_of_dependants': [input_dict['Number of Dependants']],
        'bmi_category': [input_dict['BMI Category']],
        'smoking_status': [input_dict['Smoking Status']],
        'region': [input_dict['Region']],
        'insurance_plan': [input_dict['Insurance Plan']],
        'genetical_risk': [input_dict['Genetical Risk']],
        'health_risk_score': [health_risk_score]
    }
    df = pd.DataFrame(data)
    return df

def preprocess_old(input_dict):
    health_risk_score = calculate_health_risk_score(input_dict)
    data = {
        'age': [input_dict['Age']],
        'gender': [input_dict['Gender']],
        'employment_status': [input_dict['Employment Status']],
        'income_lakhs': [input_dict['Annual Income (Lakhs)']],
        'marital_status': [input_dict['Marital Status']],
        'number_of_dependants': [input_dict['Number of Dependants']],
        'bmi_category': [input_dict['BMI Category']],
        'smoking_status': [input_dict['Smoking Status']],
        'region': [input_dict['Region']],
        'insurance_plan': [input_dict['Insurance Plan']],
        'health_risk_score': [health_risk_score]
    }
    df = pd.DataFrame(data)
    return df

def predict(input_dict):
    if input_dict['Age'] <= 25:
        input_df = preprocess_young(input_dict)
        prediction = model_young.predict(input_df)
    else:
        input_df = preprocess_old(input_dict)
        prediction = model_old.predict(input_df)
    return int(prediction[0])
