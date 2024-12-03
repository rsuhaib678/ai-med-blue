import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu
from utils import get_img_as_base64, preprocess_tabular

backgroundImg = get_img_as_base64("assets/2.png")
modelImage = get_img_as_base64("assets/eye_disease_icon.png")

# Load Models
heart_disease_model = joblib.load('models/heart_disease_model.pkl')

heart_disease_classes = ['No Disease', 'Disease']


custom_css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{backgroundImg}');
        background-size: cover;
        background-repeat: repeat;
    }}

    [data-testid="stImage"] > img {{
        width: 300px;
        height: auto;
        border-radius: 12px;
    }}

    .model-box {{
        background-color: #fff;
        padding: 16px;
        text-align: center;
        border-radius: 12px;
    }}

    .prediction-box {{
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        text-align: center;
    }}
    .prediction-box h4 {{
        font-size: 1.2rem;
        color: #000;
    }}
    .prediction-box span {{
        color: #1976D2;
    }}
    </style>
    """

st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state
if "prediction" not in st.session_state:
    st.session_state.prediction = None
    
# Create two columns for layout
col1, col2 = st.columns([2, 3], gap="large")

# Column 1: Display model image and prediction text
with col1:
    st.markdown(
    f"""
    <div class='model-box'">
        <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px; color: #000">Heart Disease Detection</div>
        <img src="data:image/png;base64,{modelImage}" alt="Brain Tumor Icon" style="width: 100%; height: auto; border-radius: 12px">
    </div>
    """,
    unsafe_allow_html=True
)
    
    
    # Prediction text will be added after the image is uploaded
    prediction_text = st.session_state.prediction or "No prediction yet"
    st.markdown(
        f"""
        <div class="prediction-box">
            <h4>Prediction: <span>{prediction_text}</span></h4>
        </div>
        """,
        unsafe_allow_html=True
    )

# Column 2: Image upload and preview
with col2:
    selected = option_menu(
    menu_title=None, 
    options=["Manual Input", "Upload CSV"], 
    icons=["pencil", "cloud-upload"], 
    menu_icon="menu",  
    default_index=0,  
    orientation="horizontal",  
)
    if selected == "Manual Input":
        # Create two columns
        col1, col2 = st.columns(2)

        # Divide inputs into two columns
        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, value=50)
            sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
            cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
            trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
            chol = st.number_input("Cholesterol", min_value=100, max_value=400, value=200)
            fbs = st.selectbox("Fasting Blood Sugar > 120 (0 = No, 1 = Yes)", [0, 1])

        with col2:
            restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
            thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=200, value=150)
            exang = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0, 1])
            oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=5.0, value=0.0, step=0.1)
            slope = st.selectbox("Slope of the Peak Exercise ST Segment (0-2)", [0, 1, 2])
            ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
        
        thal = st.selectbox("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)", [0, 1, 2])

        # Collect inputs
        heart_inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]


        # Preprocess input and predict
        heart_data = preprocess_tabular(heart_inputs)
        prediction = heart_disease_model.predict(heart_data)
        predicted_class = heart_disease_classes[int(prediction[0] > 0.5)]

        # Store the prediction in session_state to display in column 1
        if st.session_state.prediction != predicted_class:
            st.session_state.prediction = predicted_class
            st.experimental_rerun()

    elif selected == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            required_columns = [
                "age", "sex", "cp", "trestbps", "chol", "fbs",
                "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
            ]
            if all(col in df.columns for col in required_columns):
                heart_data = df[required_columns].values
                predictions = heart_disease_model.predict(heart_data)
                predicted_classes = [heart_disease_classes[int(pred > 0.5)] for pred in predictions]
                df["Prediction"] = predicted_classes
                st.dataframe(df)
            else:
                st.error("The uploaded CSV does not have the required columns. Please check your file.")