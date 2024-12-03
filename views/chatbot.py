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
            "AI-Med Models Ltd. is an Artificial Intelligence technology company based in the United Kingdom. We aim to develop artificial Intelligence in the field of medical sciences. Our team tirelessly works to create the most advanced, effective, innovative models."
            "Those creative AI models generated enhance decision-making solutions by leveraging vast data to identify patterns and trends often invisible to humans."
            "Our complex machine learning algorithms can analyze MRI, X-ray, ultrasonic, and other scans to diagnose illnesses like cancer and other serious diseases."
            "Our innovative AI models can analyze these images and data, and pick up the signs of cancer which is very difficult to see with the human eye when the cancer first develops. Diagnosing cancers at an early stage is important as this increases the chance the cancer can be treated successfully with medications and treatments. As the cancer spreads it becomes more visible in scans. This is too late to start the treatments."
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
