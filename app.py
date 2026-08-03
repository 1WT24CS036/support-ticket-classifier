import streamlit as st
import requests

BASE_URL = "https://support-ticket-classifier-1zae.onrender.com"

st.title("Support Ticket Classifier")
st.write("Submit, view, update, delete tickets here.")

# --- Submit Ticket ---
message = st.text_input("Enter your ticket message:")
if st.button("Submit"):
    response = requests.post(f"{BASE_URL}/tickets", json={"message": message})
    st.write("Response:", response.json())

# --- View Tickets ---
if st.button("View All Tickets"):
    response = requests.get(f"{BASE_URL}/tickets")
    if response.status_code == 200:
        tickets = response.json()
        for t in tickets:
            st.write(f"ID: {t['id']} | Message: {t['message']}")
    else:
        st.write("Error:", response.text)

# --- Update Ticket ---
update_id = st.number_input("Ticket ID to update:", min_value=1, step=1)
update_message = st.text_input("New message for update:")
if st.button("Update Ticket"):
    response = requests.put(f"{BASE_URL}/tickets/{update_id}", json={"message": update_message})
    st.write("Response:", response.json())

# --- Delete Ticket ---
delete_id = st.number_input("Ticket ID to delete:", min_value=1, step=1)
if st.button("Delete Ticket"):
    response = requests.delete(f"{BASE_URL}/tickets/{delete_id}")
    if response.status_code == 200:
        st.write("Ticket deleted successfully")
    else:
        st.write("Error:", response.text)
