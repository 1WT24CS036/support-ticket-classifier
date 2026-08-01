import streamlit as st
import requests

st.title("Support Ticket Classifier")
st.write("Submit, view, update, delete tickets here.")

# Input box
message = st.text_input("Enter your ticket message:")

# Submit button
if st.button("Submit"):
    response = requests.post(
        "https://support-ticket-classifier-1zae.onrender.com/tickets",
        json={"message": message}
    )
    st.write("Response:", response.json())
