import streamlit as st

# CONFIG
st.set_page_config(page_title="Personalized Political Chatbot", layout="centered")

# Customize user info
USER_NAME = "Jessica Cowles"
AVATAR_URL = "https://www.w3schools.com/howto/img_avatar2.png"

# CSS Styling
st.markdown(f"""
    <style>
    .header {{
        background-color: #001f3f;
        padding: 1rem;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
        color: white;
        display: flex;
        align-items: center;
    }}
    .header img {{
        border-radius: 50%;
        width: 40px;
        height: 40px;
        margin-right: 1rem;
    }}
    .chat-box {{
        background-color: #f1f1f1;
        height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }}
    .user-msg, .bot-msg {{
        max-width: 75%;
        padding: 0.6rem 1rem;
        margin: 0.5rem 0;
        border-radius: 20px;
        display: inline-block;
    }}
    .user-msg {{
        background-color: #001f3f;
        color: white;
        align-self: flex-end;
        margin-left: auto;
    }}
    .bot-msg {{
        background-color: #e0e0e0;
        color: black;
        align-self: flex-start;
        margin-right: auto;
    }}
    </style>
""", unsafe_allow_html=True)

# Header with avatar and name
st.markdown(f"""
    <div class='header'>
        <img src="{AVATAR_URL}" />
        <div>
            <div><strong>Chat with {USER_NAME}</strong></div>
            <small>We're online</small>
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"sender": "bot", "text": "Hi there! 👋 Nice to see you! Ask me anything about your campaign."}
    ]

# Chat display
with st.container():
    for msg in st.session_state.messages:
        role = "bot-msg" if msg["sender"] == "bot" else "user-msg"
        align = "flex-start" if msg["sender"] == "bot" else "flex-end"
        st.markdown(f"""
            <div style='display: flex; justify-content: {align};'>
                <div class='{role}'>{msg['text']}</div>
            </div>
        """, unsafe_allow_html=True)

# Input and send
col1, col2 = st.columns([9, 1])
with col1:
    user_input = st.text_input("Type your message here...", label_visibility="collapsed", key="user_input")
with col2:
    send = st.button("➤")

# Handle input
if send and user_input:
    st.session_state.messages.append({"sender": "user", "text": user_input})
    query = user_input.lower()

    # Dummy replies
    if "fundraising" in query:
        reply = "Our top fundraising goal for this quarter is $250,000 to support local outreach."
    elif "donor" in query or "new york" in query:
        reply = "Our top donors in New York include Jane Doe and Citizens for Liberty."
    elif "engagement" in query or "compare" in query:
        reply = "Compared to other PACs, our engagement has increased by 15% over the last month."
    else:
        reply = "Thanks for your question! We’ll get back to you with more info soon."

    st.session_state.messages.append({"sender": "bot", "text": reply})
    st.session_state.user_input = ""  # Clear input field
