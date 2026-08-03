# Support Ticket Classifier

A simple full‑stack project built with **FastAPI** (backend) and **Streamlit** (frontend) to manage support tickets.  
Features include login, ticket categories (Login Issue, Payment, General Query), and full CRUD operations.

---

## 🚀 Features
- **Login system** (demo credentials: `admin / 1234`)
- **Ticket categories**: Login Issue, Payment, General Query
- **CRUD operations**:
  - Submit ticket
  - View all tickets
  - Update ticket
  - Delete ticket
- **Frontend UI** with Streamlit
- **Backend API** with FastAPI
- **Deployment** on Render (both backend and frontend live)

---

## 🛠️ Tech Stack
- **Backend**: FastAPI, Pydantic
- **Frontend**: Streamlit
- **Version Control**: Git + GitHub
- **Deployment**: Render
- **Database**: In‑memory (can be extended to SQLite with SQLAlchemy)

---

## ⚙️ How to Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
