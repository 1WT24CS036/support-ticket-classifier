from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tickets = {}
ticket_counter = 0

class Ticket(BaseModel):
    message: str

@app.post("/tickets")
def create_ticket(ticket: Ticket):
    global ticket_counter
    ticket_counter += 1
    tickets[ticket_counter] = ticket.message
    return {"id": ticket_counter, "message": ticket.message}

@app.get("/tickets")
def get_tickets():
    return [{"id": tid, "message": msg} for tid, msg in tickets.items()]

@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket):
    if ticket_id in tickets:
        tickets[ticket_id] = ticket.message
        return {"id": ticket_id, "message": ticket.message}
    return {"error": "Ticket not found"}

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    if ticket_id in tickets:
        del tickets[ticket_id]
        return {"message": "Ticket deleted successfully"}
    return {"error": "Ticket not found"}
