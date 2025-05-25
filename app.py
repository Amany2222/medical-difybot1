import streamlit as st

st.set_page_config(page_title="Medical DefyBot", layout="wide")

st.title("💬 Medical DefyBot")
st.markdown("""
Welcome to **Medical DefyBot**, your smart AI assistant for health-related queries.  
This assistant is powered by Dify and built to support users with intelligent medical help.
""")

st.markdown("---")

st.markdown("### 🤖 Chat with the Bot Below:")

# Embed the Dify chat UI
dify_url = "https://api.dify.ai/v1"
st.components.v1.iframe(dify_url, height=600, scrolling=True)

st.markdown("---")
st.caption("Built by Salma | Powered by Dify + Streamlit")
