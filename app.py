# Enhanced Streamlit app code with improved UI based on the provided design

import streamlit as st

# Page configuration
st.set_page_config(page_title="Personalized Political Chatbot", layout="centered")

# Custom CSS styling
st.markdown(\"\"\"
    <style>
    .header {
        background-color: #001f3f;
        padding: 1rem;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        color: white;
        display: flex;
        align-items: center;
    }
    .header img {
        border-radius: 50%;
        width: 40px;
        height: 40px;
        margin-right: 1rem;
    }
    .chat-box {
        background-color: #f1f1f1;
        height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 15px;
        margin-bottom: 1rem;
    }
    .user-msg, .bot-msg {
        max-width: 75%;
        padding: 0.6rem 1rem;
        margin: 0.5rem 0;
        border-radius: 20px;
        display: inline-block;
    }
    .user-msg {
        background-color: #001f3f;
        color: white;
        align-self: flex-end;
        margin-left: auto;
    }
    .bot-msg {
        background-color: #e0e0e0;
        color: black;
        align-self: flex-start;
        margin-right: auto;
    }
    .input-container {
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }
    </style>
\"\"\", unsafe_allow_html=True)

# Header section
st.markdown(\"\"\"<div class='header'>
    <img src='https://www.w3schools.com/w3images/avatar2.png' />
    <div>
        <div><strong>Chat with Personalized Political Chatbot</strong></div>
        <small>We're online</small>
    </div>
</div>\"\"\", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {'sender': 'bot', 'text': "Hi there! I’m your Personalized Political Chatbot. Ask me anything about your campaign!"}
    ]

# Chat history display
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    msg_class = "bot-msg" if msg["sender"] == "bot" else "user-msg"
    st.markdown(f"<div class='{msg_class}'>{msg['text']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Input + Send button
col1, col2 = st.columns([9, 1])
with col1:
    user_input = st.text_input("Enter your message", label_visibility="collapsed", placeholder="Type your message here...")
with col2:
    send_clicked = st.button("➤")

# Generate response
if send_clicked and user_input:
    st.session_state.messages.append({'sender': 'user', 'text': user_input})
    input_lower = user_input.lower()

    # Simulated responses
    if "fundraising" in input_lower:
        reply = "Our top fundraising goal for this quarter is $250,000 to support local outreach."
    elif "donor" in input_lower or "new york" in input_lower:
        reply = "Our top donors in New York include Jane Doe and Citizens for Liberty."
    elif "engagement" in input_lower or "compare" in input_lower:
        reply = "Compared to other PACs, our engagement has increased by 15% over the last month."
    else:
        reply = "Thanks for your question! We’ll get back to you with more info soon."

    st.session_state.messages.append({'sender': 'bot', 'text': reply})
