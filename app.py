import streamlit as st

# Set page config
st.set_page_config(page_title="Political Chatbot", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    .header {
        background-color: #001f3f;
        padding: 1rem;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        text-align: center;
    }
    .chat-box {
        background-color: #f1f1f1;
        height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-msg, .bot-msg {
        max-width: 75%;
        padding: 0.5rem;
        border-radius: 10px;
        margin: 0.25rem 0;
    }
    .user-msg {
        background-color: #cce5ff;
        align-self: flex-end;
    }
    .bot-msg {
        background-color: #ffffff;
        align-self: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='header'>POLITICAL CHATBOT</div>
""", unsafe_allow_html=True)

# Chat state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Input field
user_input = st.text_input("Ask me anything about your campaign:", key="user_input")

# Basic scripted responses (GPT-3.5 placeholder logic)
def get_response(prompt):
    prompt = prompt.lower()
    if "top donors" in prompt and "new york" in prompt:
        return "Our top donors in New York include Jane Doe and Citizens for Liberty."
    elif "doors" in prompt and "pennsylvania" in prompt:
        return "We knocked on 8,245 doors in Pennsylvania this week."
    elif "canvassing contact rate" in prompt and "georgia" in prompt:
        return "The canvassing contact rate in Georgia is currently 43%."
    else:
        return "I'm not sure about that yet, but more features are coming soon!"

# Handle user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
    st.experimental_rerun()
