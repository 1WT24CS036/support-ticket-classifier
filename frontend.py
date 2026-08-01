import requests
import streamlit as st

user_input = st.text_input("Enter Support Ticket Description")

if st.button("Classify Ticket"):
    response = requests.post(
        "https://support-ticket-classifier-1zae.onrender.com/classify",
        json={"description": user_input}
    )
    result = response.json()
    st.write("Ticket Category:", result["category"])
    st.write("Ticket Priority:", result["priority"])
