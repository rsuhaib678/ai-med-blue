import streamlit as st

# App Styling
st.set_page_config(page_title="AI-MED Models UK", page_icon="🩺")

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

custom_css = """
<style>
[data-testid="stHeader"] {
    background: transparent;
}

/* Customize the sidebar background */
[data-testid="stSidebar"] {
    width: 300px !important;
    border-right: 2px solid rgb(238, 238, 238);
    background: #fff;
}

[data-testid="stAppViewBlockContainer"] {
    max-width: 70rem;
    padding: 6rem 1rem 4rem;
}

[data-testid="stLogo"] {
    width: 150px;
    height: auto;
    margin: 0 auto 24px;
}

[data-testid="stSidebarNavItems"] > li {
    margin: 16px 0;
}

[data-testid="stSidebarNavLink"] {
    border-radius: 12px;
    padding: 4px 12px;
    gap: 20px;
}
[data-testid="stSidebarNavLink"]:hover {
    border-radius: 12px;
    # background: #cee1ff;
}

[data-testid="stIconMaterial"] {
    font-size: 20px;
}

[data-testid="stSidebarUserContent"] {
    padding: 16px;
    position: absolute;
    bottom: 0;
    width: 100%;
}

/* Styling for the top navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f9f9f9;
    padding: 10px 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}
.navbar .title {
    font-size: 20px;
    font-weight: bold;
    color: #333;
}
.navbar .link-button {
    text-decoration: none;
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.navbar .link-button:hover {
    background-color: #0056b3;
}

/* Footer styling inside the sidebar */
.sidebar-footer {
    margin-top: auto;
    padding-top: 20px;
    text-align: center;
    font-size: 12px;
}
.sidebar-footer .footer-title {
    font-weight: bold;
    font-size: 14px;
    margin-bottom: 8px;
}
.sidebar-footer .footer-subtitle {
    font-size: 14px;
    font-style: italic;
}
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# --- PAGE SETUP ---
home_page = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
project_1_page = st.Page(
    "views/brain-tumor.py",
    title="Brain Tumor",
    icon=":material/neurology:",
)
project_2_page = st.Page(
    "views/lung-cancer.py",
    title="Lung Cancer",
    icon=":material/pulmonology:",
)
project_3_page = st.Page(
    "views/eye-disease.py",
    title="Eye Disease",
    icon=":material/visibility:",
)
project_4_page = st.Page(
    "views/heart-disease.py",
    title="Heart Disease",
    icon=":material/favorite:",
)
project_5_page = st.Page(
    "views/breast-cancer.py",
    title="Breast Cancer",
    icon=":material/female:",
)
project_6_page = st.Page(
    "views/chatbot.py",
    title="Diagnostic GPT",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[home_page, project_1_page, project_2_page, project_3_page, project_4_page, project_5_page, project_6_page])


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo.png")

st.sidebar.markdown(
    """
    <div class="sidebar-footer">
        <p class="footer-title">&copy; 2024 AI-MED Models UK</p>
        <p class="footer-subtitle">Transforming Healthcare with AI</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --- RUN NAVIGATION ---
pg.run()
