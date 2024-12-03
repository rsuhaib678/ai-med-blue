import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu
from utils import get_img_as_base64, preprocess_tabular

backgroundImg = get_img_as_base64("assets/bg4IMG.png")
modelImage = get_img_as_base64("assets/breast_cancer_icon.png")

# Load Models
breast_cancer_model = load_model('models/breast_cancer_model.h5', compile=False)
breast_cancer_scaler = joblib.load('models/breast_cancer_scaler.pkl')
breast_cancer_classes = ['Malignant', 'Benign']

custom_css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url('data:image/png;base64,{backgroundImg}');
        background-position: top right;
        background-repeat: repeat;
        background-size: 25% auto;
    }}

    [data-testid="stImage"] > img {{
        width: 300px;
        height: auto;
        border-radius: 12px;
    }}

    [data-testid="stFileUploader"] {{
        max-width: 600px;
        margin: auto;
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
        margin-top: 20px;
        text-align: center;
        width: 100%;
    }}
    .prediction-box h4 {{
        font-size: 1.2rem;
        color: #000;
    }}
    .prediction-box span {{
        color: #1976D2;
    }}

    /* Centering the first column content */
    .first-column-content {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        max-width: 350px;
        width: 100%;
        # height: 100%;
        margin: auto;
        text-align: center;
    }}

    /* Centering the second column content */
    .second-column-content {{
        margin-top: 20px;
        display: block;
        text-align: center;
    }}

    .border {{
        border: dotted #FFF 10px;
        border-bottom: none;
        # width: 30%;
        margin: 50px auto;
    }}
    </style>
    """

st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state
if "prediction" not in st.session_state:
    st.session_state.prediction = None


prediction_text = st.session_state.prediction or "No prediction yet"
st.markdown(
    f"""
    <div class="first-column-content">
        <div class='model-box'>
            <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px; color: #000">Breast Cancer Detection</div>
            <img src="data:image/png;base64,{modelImage}" alt="Breast Cancer Icon" style="width: 100%; height: auto; border-radius: 12px">
        </div>
        <div class="prediction-box">
        <h4>Prediction: <span>{prediction_text}</span></h4>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"<hr class='border'></hr>", unsafe_allow_html=True)

# Options menu for manual input or CSV upload
selected = option_menu(
    menu_title=None,  
    options=["Manual Input", "Upload CSV"],  
    icons=["pencil", "cloud-upload"],  
    menu_icon="menu",  
    default_index=0,  
    orientation="horizontal",
    styles={
        "container": {"max-width": "600px"},
        # "icon": {"color": "orange", "font-size": "16px"}, 
        # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        # "nav-link-selected": {"background-color": "#FB8C00"},
    }  
)

if selected == "Manual Input":
    # Create three columns
        col1, col2, col3 = st.columns(3)

        # Divide inputs across the three columns
        with col1:
            breast_inputs = [
                st.number_input("Radius Mean", value=14.0),
                st.number_input("Texture Mean", value=19.0),
                st.number_input("Perimeter Mean", value=90.0),
                st.number_input("Area Mean", value=600.0),
                st.number_input("Smoothness Mean", value=0.1),
                st.number_input("Compactness Mean", value=0.2),
                st.number_input("Concavity Mean", value=0.3),
                st.number_input("Concave Points Mean", value=0.1),
                st.number_input("Symmetry Mean", value=0.2),
                st.number_input("Fractal Dimension Mean", value=0.07)
            ]

        with col2:
            breast_inputs += [
                st.number_input("Radius SE", value=0.5),
                st.number_input("Texture SE", value=1.0),
                st.number_input("Perimeter SE", value=3.0),
                st.number_input("Area SE", value=20.0),
                st.number_input("Smoothness SE", value=0.005),
                st.number_input("Compactness SE", value=0.02),
                st.number_input("Concavity SE", value=0.03),
                st.number_input("Concave Points SE", value=0.01),
                st.number_input("Symmetry SE", value=0.02),
                st.number_input("Fractal Dimension SE", value=0.002)
            ]

        with col3:
            breast_inputs += [
                st.number_input("Radius Worst", value=15.0),
                st.number_input("Texture Worst", value=25.0),
                st.number_input("Perimeter Worst", value=100.0),
                st.number_input("Area Worst", value=800.0),
                st.number_input("Smoothness Worst", value=0.15),
                st.number_input("Compactness Worst", value=0.25),
                st.number_input("Concavity Worst", value=0.35),
                st.number_input("Concave Points Worst", value=0.15),
                st.number_input("Symmetry Worst", value=0.3),
                st.number_input("Fractal Dimension Worst", value=0.08)
            ]

        # Preprocess and predict
        breast_data = preprocess_tabular(breast_inputs, scaler=breast_cancer_scaler)
        prediction = breast_cancer_model.predict(breast_data)
        predicted_class = breast_cancer_classes[int(prediction[0][0] > 0.5)]  # Use 0.5 threshold

        # Store the prediction in session_state to display in column 1
        if st.session_state.prediction != predicted_class:
            st.session_state.prediction = predicted_class
            st.experimental_rerun()

elif selected == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="breast_cancer_csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if df.shape[1] == 30:  # Ensure correct number of features
            breast_data = breast_cancer_scaler.transform(df)
            predictions = breast_cancer_model.predict(breast_data)
            predicted_classes = [breast_cancer_classes[int(pred[0] > 0.5)] for pred in predictions]
            df["Prediction"] = predicted_classes

            # Display the results
            st.markdown("<h4 style='text-align: center;'>Batch Predictions:</h4>", unsafe_allow_html=True)
            st.dataframe(df)
        else:
            st.error("The uploaded CSV does not have the required 30 features. Please check your file.")
