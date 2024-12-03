import random
import time

import streamlit as st

custom_css = """
<style>
/* Center headings and other elements on smaller devices */
[data-testid="stChatMessage"] {
    background: #fff
}
</style>
"""

# Apply the common CSS globally
st.markdown(custom_css, unsafe_allow_html=True)


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Aimed is a rapidly growing software startup specializing in artificial intelligence (AI) solutions for the healthcare industry. Partner companies founded in 2021, the company has developed a proprietary AI healthcare platform that enhances diagnostic improves patients outcome by optimising treatment plans and predicting potential health issues before comes to critical stages."
            "Artificial Intelligence (AI) and modeling have emerged as powerful tools reshaping numerous sectors in our increasingly digital world, explores the wide-ranging applications of AI-powered modeling across various industries, highlighting its transformative impact and potential for future growth."
            "The global AI in healthcare market is expected to grow from US$6.7 billion in 2021 to US$45.2 billion by 2026, at a CAGR of 46.2%. The increasing demand for personalized medicine, the need to reduce healthcare costs, and the availability of large data sets for machine learning are key drivers of this growth."
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
