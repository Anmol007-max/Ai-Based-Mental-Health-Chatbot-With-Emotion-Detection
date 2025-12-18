# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("MINDBOT - AI Mental Health Therapist")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step2: User is able to ask question
# Chat input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # AI Agent exists here
    try:
        response = requests.post(BACKEND_URL, json={"message": user_input}, timeout=60)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        
        tool_info = f" [Tool: {data['tool_called']}]" if data.get('tool_called') != 'None' else ""
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": f"{data['response']}{tool_info}"
        })
    except requests.exceptions.RequestException as e:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": f"❌ Error connecting to backend: {str(e)}"
        })
    except Exception as e:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": f"❌ Error: {str(e)}"
        })


# Step3: Show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])