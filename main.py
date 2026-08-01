from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ---------------------------
# Create FastAPI app
# ---------------------------
app = FastAPI()

# ---------------------------
# Enable CORS
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Database setup
# ---------------------------
DATABASE_URL = "sqlite:///./tickets.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ---------------------------
# Ticket table
# ---------------------------
class TicketDB(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    intent = Column(String, index=True)

Base.metadata.create_all(bind=engine)

# ---------------------------
# Pydantic model
# ---------------------------
class Ticket(BaseModel):
    message: str

# ---------------------------
# Dependency
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# Intent classifier
# ---------------------------
def classify_intent(message: str) -> str:
    message_lower = message.lower()
    if "login" in message_lower or "password" in message_lower:
        return "login_issue"
    elif "payment" in message_lower or "card" in message_lower:
        return "payment_issue"
    elif "crash" in message_lower or "error" in message_lower:
        return "technical_issue"
    else:
        return "general_query"

# ---------------------------
# Endpoints
# ---------------------------

# Create ticket
@app.post("/tickets")
def create_ticket(ticket: Ticket, db: Session = Depends(get_db)):
    intent = classify_intent(ticket.message)   # <-- classifier used here
    db_ticket = TicketDB(message=ticket.message, intent=intent)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {"id": db_ticket.id, "original_message": db_ticket.message, "intent": db_ticket.intent}

# Get all tickets
@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(TicketDB).all()
    return {"tickets": [{"id": t.id, "message": t.message, "intent": t.intent} for t in tickets]}

# Update ticket
@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket, db: Session = Depends(get_db)):
    db_ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()
    if db_ticket is None:
        return {"error": "Ticket not found"}
    db_ticket.message = ticket.message
    db_ticket.intent = classify_intent(ticket.message)   # <-- reclassify on update
    db.commit()
    db.refresh(db_ticket)
    return {"id": db_ticket.id, "message": db_ticket.message, "intent": db_ticket.intent}

# Delete ticket
@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()
    if db_ticket is None:
        return {"error": "Ticket not found"}
    db.delete(db_ticket)
    db.commit()
    return {"message": f"Ticket {ticket_id} deleted successfully"}
