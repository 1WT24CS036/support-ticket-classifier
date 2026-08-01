import streamlit as st

# Background options
backgrounds = {
    "Tech Theme": "https://images.unsplash.com/photo-1518770660439-4636190af475",
    "Office Theme": "https://images.unsplash.com/photo-1521791136064-7986c2920216",
    "Abstract Colors": "https://images.unsplash.com/photo-1503264116251-35a269479413",
    "Dark Mode": "https://images.unsplash.com/photo-1505685296765-3a2736de412f"
}

choice = st.selectbox("Choose a background:", list(backgrounds.keys()))

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{backgrounds[choice]}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🎟️ Support Ticket System")


st.title("🎟️ Support Ticket System")

# Create Ticket
message = st.text_input("Enter your ticket:")
if st.button("Submit Ticket"):
    response = requests.post(f"{BASE_URL}/tickets", json={"message": message})
    st.write("Response:", response.json())

# View Tickets
if st.button("View All Tickets"):
    response = requests.get(f"{BASE_URL}/tickets")
    st.write("Tickets:", response.json())

# Update Ticket
ticket_id = st.number_input("Ticket ID to update:", min_value=1, step=1)
new_message = st.text_input("New message:")
if st.button("Update Ticket"):
    response = requests.put(f"{BASE_URL}/tickets/{ticket_id}", json={"message": new_message})
    st.write("Updated:", response.json())

# Delete Ticket
delete_id = st.number_input("Ticket ID to delete:", min_value=1, step=1)
if st.button("Delete Ticket"):
    response = requests.delete(f"{BASE_URL}/tickets/{delete_id}")
    st.write("Deleted:", response.json())
