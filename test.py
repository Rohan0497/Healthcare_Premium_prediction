# codebasics ML course: codebasics.io, all rights reserved

import streamlit as st
from prediction_helper import predict

# Page configuration
st.set_page_config(page_title="🩺 Health Insurance Cost Predictor", page_icon="💸", layout="wide")

# Sidebar with instructions
st.sidebar.header("📘 How to Use")
st.sidebar.write("""
1. Fill in the user details across age, lifestyle, and medical background.
2. Click **Predict** to estimate health insurance cost.
3. Results will be displayed below the button.
""")
st.sidebar.info("🔒 Your inputs are not stored or shared.")

# Title
st.markdown("<h1 style='text-align: center; color: teal;'>🩺 Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Estimate your expected insurance cost based on personal and medical factors</h4>", unsafe_allow_html=True)
st.markdown("---")

# Define layout rows
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Dropdown options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Input fields
with row1[0]:
    age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('👨‍👩‍👧 Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('💰 Income (Lakhs)', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('🧬 Genetical Risk (0-5)', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('📦 Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('⚧ Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('🗺️ Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

# Input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction button
st.markdown("---")
if st.button('🔮 Predict Insurance Cost'):
    prediction = predict(input_dict)
    
    # Display result in a colored card
    st.success("✅ Prediction Complete!")
    st.markdown(f"""
        <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;border:1px solid #b3d1ff;">
            <h3 style="color:#003366;">💵 Predicted Insurance Cost:</h3>
            <h2 style="color:#008080;">₹ {prediction}</h2>
        </div>
    """, unsafe_allow_html=True)

    # Extra interpretation (optional, rule-based)
    if prediction > 50000:
        st.warning("⚠️ This is a relatively high premium. Consider reviewing risk factors such as smoking status, age, or pre-existing conditions.")
    else:
        st.info("🎉 Your predicted premium is within an affordable range.")

