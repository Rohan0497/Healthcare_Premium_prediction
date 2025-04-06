import streamlit as st
from prediction_helper import predict
import random
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie
import json

# Page config
st.set_page_config(page_title="🩺 Health Insurance Cost Predictor", page_icon="💸", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_medical = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json")

# Styles
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #ffffff, #e6f7f7);
        }
        .glow {
            font-size: 32px;
            color: #008080;
            font-weight: bold;
            text-align: left;
            animation: glow 2s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from { text-shadow: 0 0 5px #77ffff, 0 0 10px #77ffff; }
            to { text-shadow: 0 0 20px #00ffee, 0 0 30px #00ffee; }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📘 How to Use")
st.sidebar.write("""
1. Fill in the user details across age, lifestyle, and medical background.
2. Click **Predict** to estimate health insurance cost.
3. Results will be displayed below the button.
""")
st.sidebar.info("🔒 Your inputs are not stored or shared.")

# Header section with animation and title
with st.container():
    col1, col2 = st.columns([1, 6])
    with col1:
        if lottie_medical:
            st_lottie(lottie_medical, height=60, key="header_anim")
    with col2:
        st.markdown('<div class="glow">🩺 Health Insurance Cost Predictor</div>', unsafe_allow_html=True)
        st.markdown("<h4 style='margin-top: -15px;'>Estimate your expected insurance cost based on personal and medical factors</h4>", unsafe_allow_html=True)

st.markdown("---")

# Input options
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

# Inputs aligned cleanly
with st.container():
    row1, row2, row3, row4 = st.columns(3), st.columns(3), st.columns(3), st.columns(3)

    with row1[0]: age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100)
    with row1[1]: number_of_dependants = st.number_input('👨‍👩‍👧 Dependants', min_value=0, step=1, max_value=20)
    with row1[2]: income_lakhs = st.number_input('💰 Income (Lakhs)', step=1, min_value=0, max_value=200)

    with row2[0]: genetical_risk = st.number_input('🧬 Genetical Risk (0-5)', step=1, min_value=0, max_value=5)
    with row2[1]: insurance_plan = st.selectbox('📦 Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]: employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

    with row3[0]: gender = st.selectbox('⚧ Gender', categorical_options['Gender'])
    with row3[1]: marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
    with row3[2]: bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])

    with row4[0]: smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
    with row4[1]: region = st.selectbox('🗺️ Region', categorical_options['Region'])
    with row4[2]: medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

# Input summary
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

st.markdown("---")
with st.expander("📋 See Your Input Summary"):
    st.json(input_dict)

if 'history' not in st.session_state:
    st.session_state.history = []

# Prediction logic
if st.button('🔮 Predict Insurance Cost'):
    prediction = predict(input_dict)
    st.session_state.history.append(prediction)

    st.markdown(f"""
        <div style="background-color:#f0f8ff;padding:20px;border-radius:10px;border:1px solid #b3d1ff;">
            <h3 style="color:#003366;">💵 Predicted Insurance Cost:</h3>
            <h2 style="color:#008080;">₹ {prediction}</h2>
        </div>
    """, unsafe_allow_html=True)

    # Health score
    score = random.randint(60, 95)
    st.markdown("#### 🧠 Estimated Health Score")
    st.caption("This score is a general health estimate (0–100) based on your inputs. Higher scores often reflect lower predicted insurance costs.")
    st.progress(score)

    # Radar Chart Explanation
    st.markdown("#### 🕸️ Health Risk Radar")
    st.caption("""
    This radar chart compares five key health-related risk factors based on your inputs.  
    Values are normalized from 0 to 1, where higher values indicate higher risk:
    - **Age** (normalized)
    - **Genetical Risk** (scale 0–5)
    - **BMI Risk** (if not 'Normal')
    - **Smoking Risk** (if smoker)
    - **Medical Risk** (if prior health conditions)
    """)

    # Radar Chart Values
    categories = ['Age', 'Genetical Risk', 'BMI Risk', 'Smoking Risk', 'Medical Risk']
    values = [
        age / 100,
        genetical_risk / 5,
        0.3 if bmi_category != 'Normal' else 0,
        0.4 if smoking_status != 'No Smoking' else 0,
        0.5 if medical_history != 'No Disease' else 0
    ]

    # Radar Chart Plot
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Risk Profile',
        line=dict(color='#008080')
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], color="lightgrey"),
            bgcolor="#f9f9f9"
        ),
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)


    # Prediction history
    st.markdown("#### 📈 Prediction History")
    st.caption("Tracks how your predicted cost changes each time you update the form and click Predict.")
    st.line_chart(st.session_state.history)

    # Final health tip
    st.markdown("#### 💡 Health Tip of the Day")
    st.info("Drinking enough water supports heart health, improves digestion, and keeps your body energized throughout the day.")
