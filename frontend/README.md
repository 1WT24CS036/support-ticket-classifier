# Support Ticket Classifier - Frontend

This is the **Streamlit frontend** for the Support Ticket Classifier project.  
It provides a simple user interface to interact with the FastAPI backend, allowing users to log in, submit tickets, view, update, and delete them.

---

## 🚀 Features
- **Login page** (demo credentials: `admin / 1234`)
- **Submit Ticket** with category selection:
  - Login Issue
  - Payment
  - General Query
- **View Tickets** list
- **Update Ticket** (edit message + category)
- **Delete Ticket**
- **Sidebar navigation** for easy access
- **Custom background styling**

---

## 🛠️ Tech Stack
- **Frontend Framework**: Streamlit
- **HTTP Requests**: Python `requests` library
- **Backend API**: FastAPI (deployed separately)
- **Deployment**: Render

---

## ⚙️ How to Run Locally

### Install dependencies
```bash
cd frontend
pip install -r requirements.txt
