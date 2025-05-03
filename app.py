st.markdown("""
    <style>
    .chat-box {
        background-color: #f9f9f9;
        height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 12px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }

    .user-msg, .bot-msg {
        max-width: 80%;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 18px;
        font-size: 0.95rem;
        line-height: 1.4;
        position: relative;
    }

    .user-msg {
        background-color: #001f3f;
        color: white;
        align-self: flex-end;
        margin-left: auto;
        border-bottom-right-radius: 4px;
    }

    .bot-msg {
        background-color: #eef2ff;
        color: #000;
        align-self: flex-start;
        margin-right: auto;
        border-bottom-left-radius: 4px;
    }

    .bot-msg::after {
        content: "Answered by AI";
        display: block;
        font-size: 0.7rem;
        margin-top: 0.25rem;
        color: #555;
    }

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
    </style>
""", unsafe_allow_html=True)
