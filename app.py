import streamlit as st
import requests

# Base URL for backend API
BASE_URL = "https://support-ticket-classifier-2-jj14.onrender.com"

st.title("Support Ticket Classifier")
st.write("Submit, view, update, delete tickets here.")

# --- Submit a Ticket ---
ticket_message = st.text_input("Enter your ticket message:")
if st.button("Submit"):
    response = requests.post(f"{BASE_URL}/tickets", json={"message": ticket_message})
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code} {response.text}")

# --- View All Tickets ---
if st.button("View All Tickets"):
    response = requests.get(f"{BASE_URL}/tickets")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code} {response.text}")

# --- Update a Ticket ---
ticket_id_update = st.text_input("Ticket ID to update:")
new_message = st.text_input("New message for update:")
if st.button("Update Ticket"):
    response = requests.put(f"{BASE_URL}/tickets/{ticket_id_update}", json={"message": new_message})
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code} {response.text}")

# --- Delete a Ticket ---
ticket_id_delete = st.text_input("Ticket ID to delete:")
if st.button("Delete Ticket"):
    response = requests.delete(f"{BASE_URL}/tickets/{ticket_id_delete}")
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code} {response.text}")
