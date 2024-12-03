import streamlit as st

st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; background-color:#fff; padding: 20px; border-radius: 16px; margin-bottom: 4rem;">
        <h1 style="margin: 0; padding:0;">Welcome to</h1>
        <h1 style="margin: 0; padding:0;">AI-MED Models UK</h1>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<h3>AI-MED Models</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:justify;'>AI-Med Models Ltd. is an Artificial Intelligence technology company based in the United Kingdom, aimed at the development of artificial Intelligence in the field of medical sciences, our team tirelessly works to create the most advanced, effective, innovative models.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:justify;'>Those creative AI models generated enhance decision-making solutions by leveraging vast data to identify patterns and trends often invisible to humans.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:justify;'>Our complex machine learning algorithms can analyze MRI, X-ray, ultrasonic and other scans to diagnose illnesses like cancer and other serious  diseases.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:justify;'>Our innovative AI models can analyze these images and data, and pick up the signs of cancer which is very difficult to see with the human eye when the cancer first develops. Diagnosing cancers at an early stage is important as this increases the chance the cancer can be treated successfully with medications and treatments. As the cancer spreads it becomes more visible in scans. This is too late to start the treatments.</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3>Why Choose AI-MED Models?</h3>", unsafe_allow_html=True)

    # Add feature points with icons and text
    st.markdown("""
        <div style="color: #000">
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-heart" style="color: #0D47A1; font-size: 20px;"></i>
                <span style="font-size: 16px;">Early disease detection through analysis of medical imaging and patient data.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-user-md" style="color: #0D47A1; font-size: 20px;"></i>
                <span style="font-size: 16px;">Personalized treatment plans based on genetic information and patient history.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                 <i class="fas fa-capsules" style="color: #0D47A1; font-size: 20px;"></i>
                <span style="font-size: 16px;">Drug discovery and development optimization.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="far fa-hospital" style="color: #0D47A1; font-size: 20px;"></i>
                <span style="font-size: 16px;">Hospital resource management and patient flow prediction.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-shield-alt" style="color: #0D47A1; font-size: 20px;"></i>
                <span style="font-size: 16px;">Epidemic outbreak forecasting and management.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)



# Add a "Visit Us" button at the end
st.markdown("""
    <div style="text-align:center; margin-top: 2rem;">
        <a href="https://www.aimedmodels.com" target="_blank">
            <button style="
                background-color: #0D47A1; 
                color: white; 
                font-size: 16px; 
                padding: 15px 30px; 
                border-radius: 12px; 
                border: none; 
                cursor: pointer;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s;">
                Visit AI-MED Models
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

custom_css = """
<style>
/* Center headings and other elements on smaller devices */
@media (max-width: 768px) {
    h1, h2, h3, h4, h5, h6, .responsive-center {
        text-align: center !important;
    }
}
</style>
"""

# Apply the common CSS globally
st.markdown(custom_css, unsafe_allow_html=True)