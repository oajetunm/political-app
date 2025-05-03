
import streamlit as st

st.set_page_config(page_title="Personalized Political Chatbot", layout="centered")

st.markdown("""<h1 style='color:#001f3f;'>Personalized Political Chatbot</h1>""", unsafe_allow_html=True)
st.write("Ask me anything about your campaign. This is a demo with dummy data.")

user_input = st.text_input("Your question")

if user_input:
    lower_input = user_input.lower()
    if "fundraising" in lower_input:
        response = "Our top fundraising goal for this quarter is $250,000 to support local outreach."
    elif "donor" in lower_input or "new york" in lower_input:
        response = "Our top donors in New York include Jane Doe and Citizens for Liberty."
    elif "engagement" in lower_input or "compare" in lower_input:
        response = "Compared to other PACs, our engagement has increased by 15% over the last month."
    else:
        response = "Thanks for your question! We’ll get back to you with more info soon."
    st.markdown(f"**Chatbot:** {response}")
