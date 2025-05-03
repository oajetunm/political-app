import streamlit as st

# Set page configuration
st.set_page_config(page_title="Personalized Political Chatbot", layout="centered")

# Custom CSS styling
st.markdown("""
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
        display: flex;
        flex-direction: column;
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
    </style>
""", unsafe_allow_html=True)

# Header UI
st.markdown("""
<div class='header'>
    <img src='https://www.w3schools.com/w3images/avatar2.png' />
    <div>
        <div><strong>Chat with Personalized Political Chatbot</strong></div>
        <small>We're online</small>
    </div>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"sender": "bot", "text": "Hi there! I’m your Personalized Political Chatbot. Ask me anything about your campaign!"}
    ]

# Display chat history
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    role = "bot-msg" if msg["sender"] == "bot" else "user-msg"
    st.markdown(f"<div class='{role}'>{msg['text']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Input and send button
col1, col2 = st.columns([9, 1])
with col1:
    user_input = st.text_input("Type your message here...", label_visibility="collapsed")
with col2:
    send = st.button("➤")

# Handle response
if send and user_input:
    st.session_state.messages.append({"sender": "user", "text": user_input})
    query = user_input.lower()

    # Dummy responses
    if "fundraising" in query:
        reply = "Our top fundraising goal for this quarter is $250,000 to support local outreach."
    elif "donor" in query or "new york" in query:
        reply = "Our top donors in New York include Jane Doe and Citizens for Liberty."
    elif "engagement" in query or "compare" in query:
        reply = "Compared to other PACs, our engagement has increased by 15% over the last month."
    else:
        reply = "Thanks for your question! We’ll get back to you with more info soon."

    st.session_state.messages.append({"sender": "bot", "text": reply})
