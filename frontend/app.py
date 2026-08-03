import streamlit as st
import requests

BASE_URL = "https://support-ticket-classifier-2-jb14.onrender.com"

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Submit Ticket", "View Tickets", "Update Ticket", "Delete Ticket"])

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

if page == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        st.write(response.json())

elif page == "Submit Ticket":
    ticket_message = st.text_input("Enter your ticket message:")
    ticket_category = st.selectbox("Select category:", ["Login Issue", "Payment", "General Query"])
    if st.button("Submit"):
        response = requests.post(f"{BASE_URL}/tickets", json={"message": ticket_message, "category": ticket_category})
        st.write(response.json())

elif page == "View Tickets":
    if st.button("View All Tickets"):
        response = requests.get(f"{BASE_URL}/tickets")
        st.write(response.json())

elif page == "Update Ticket":
    ticket_id_update = st.text_input("Ticket ID to update:")
    new_message = st.text_input("New message for update:")
    new_category = st.selectbox("New category:", ["Login Issue", "Payment", "General Query"])
    if st.button("Update Ticket"):
        response = requests.put(f"{BASE_URL}/tickets/{ticket_id_update}", json={"message": new_message, "category": new_category})
        st.write(response.json())

elif page == "Delete Ticket":
    ticket_id_delete = st.text_input("Ticket ID to delete:")
    if st.button("Delete Ticket"):
        response = requests.delete(f"{BASE_URL}/tickets/{ticket_id_delete}")
        st.write(response.json())
