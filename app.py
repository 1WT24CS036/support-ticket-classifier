import streamlit as st
import requests

BASE_URL = "https://support-ticket-classifier-2-jj14.onrender.com"

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Submit Ticket", "View Tickets", "Update Ticket", "Delete Ticket"])

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1521791136064-7986c2920216");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Support Ticket Classifier")

if page == "Submit Ticket":
    ticket_message = st.text_input("Enter your ticket message:")
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/tickets", json={"message": ticket_message})
        st.write(response.json())

elif page == "View Tickets":
    if st.button("View All Tickets"):
        response = requests.get(f"{BASE_URL}/tickets")
        st.write(response.json())

elif page == "Update Ticket":
    ticket_id_update = st.text_input("Ticket ID to update:")
    new_message = st.text_input("New message for update:")
    if st.button("Update Ticket"):
        response = requests.put(f"{BASE_URL}/tickets/{ticket_id_update}", json={"message": new_message})
        st.write(response.json())

elif page == "Delete Ticket":
    ticket_id_delete = st.text_input("Ticket ID to delete:")
    if st.button("Delete Ticket"):
        response = requests.delete(f"{BASE_URL}/tickets/{ticket_id_delete}")
        st.write(response.json())
