import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Medical Dify Chatbot", page_icon="💬")

# Title and instructions
st.title("🩺 Medical Chatbot")
st.write("Ask any medical-related question and get helpful AI-powered answers. Please consult a professional for critical health issues.")

# Input field
user_input = st.text_input("You:", "")

# Display chat history (optional)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Send query when input is entered
if user_input:
    st.session_state.chat_history.append(("You", user_input))

    # Call the Dify API (replace the values with your real API URL and key)
    api_url = "https://api.dify.ai/v1/chat-messages"
    api_key = "a80e08c9-119f-407d-9a68-363ec23e849e"  # 
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},  # Use if your Dify app has input variables
        "query": user_input
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        answer = response.json().get("answer", "Sorry, I didn't get that.")
    else:
        answer = "Error contacting the AI service."

    st.session_state.chat_history.append(("Bot", answer))

# Display the chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"You: {message}")
    else:
        st.markdown(f"Bot: {message}")
