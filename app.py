import streamlit as st
import requests

BASE_URL = "https://support-ticket-classifier-1zae.onrender.com"

st.title("🎫 Support Ticket Classifier")

# --- Submit Ticket ---
st.header("Submit a Ticket")
message = st.text_input("Enter your issue")
if st.button("Submit Ticket"):
    if message:
        response = requests.post(f"{BASE_URL}/tickets", json={"message": message})
        st.json(response.json())
    else:
        st.warning("Please enter a message before submitting.")

# --- View Tickets ---
st.header("View All Tickets")
if st.button("View Tickets"):
    response = requests.get(f"{BASE_URL}/tickets")
    st.json(response.json())

# --- Update Ticket ---
st.header("Update a Ticket")
ticket_id_update = st.number_input("Ticket ID to update", min_value=1, step=1)
new_message = st.text_input("New message")
if st.button("Update Ticket"):
    if new_message:
        response = requests.put(
            f"{BASE_URL}/tickets/{ticket_id_update}",
            json={"message": new_message}
        )
        st.json(response.json())
    else:
        st.warning("Please enter a new message to update.")

# --- Delete Ticket ---
st.header("Delete a Ticket")
ticket_id_delete = st.number_input("Ticket ID to delete", min_value=1, step=1)
if st.button("Delete Ticket"):
    response = requests.delete(f"{BASE_URL}/tickets/{ticket_id_delete}")
    st.json(response.json())
