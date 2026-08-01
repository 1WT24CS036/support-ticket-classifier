import requests

BASE_URL = "http://127.0.0.1:8080"

# POST → Create a ticket
response = requests.post(f"{BASE_URL}/tickets", json={"message": "I forgot my password"})
print("POST:", response.json())

# GET → Retrieve all tickets
response = requests.get(f"{BASE_URL}/tickets")
print("GET:", response.json())

# PUT → Update a ticket (example: ticket with ID 1)
response = requests.put(f"{BASE_URL}/tickets/1", json={"message": "My payment failed"})
print("PUT:", response.json())

# DELETE → Remove a ticket (example: ticket with ID 1)
response = requests.delete(f"{BASE_URL}/tickets/1")
print("DELETE:", response.json())
