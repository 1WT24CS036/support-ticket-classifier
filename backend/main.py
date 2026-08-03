from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Homepage route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Support Ticket Classifier API. Use /tickets endpoints."}

# In-memory storage
tickets = {}
ticket_counter = 0

class Ticket(BaseModel):
    message: str
    category: str   # e.g., "Login Issue", "Payment", "General Query"

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    # Demo login check
    if user.username == "admin" and user.password == "1234":
        return {"message": "Login successful"}
    return {"error": "Invalid credentials"}

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    global ticket_counter
    ticket_counter += 1
    tickets[ticket_counter] = {"message": ticket.message, "category": ticket.category}
    return {"id": ticket_counter, "message": ticket.message, "category": ticket.category}

@app.get("/tickets")
def get_tickets():
    return [{"id": tid, "message": data["message"], "category": data["category"]} for tid, data in tickets.items()]

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket):
    if ticket_id in tickets:
        tickets[ticket_id] = {"message": ticket.message, "category": ticket.category}
        return {"id": ticket_id, "message": ticket.message, "category": ticket.category}
    return {"error": "Ticket not found"}

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    if ticket_id in tickets:
        del tickets[ticket_id]
        return {"message": "Ticket deleted successfully"}
    return {"error": "Ticket not found"}
