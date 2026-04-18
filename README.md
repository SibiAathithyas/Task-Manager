# Task Management System (FastAPI)

This project is a simple Task Management System built using FastAPI. The main goal was to design a clean backend with authentication and task management features, along with a minimal frontend to demonstrate how the system works end-to-end.

---
## Live Demo

Frontend: https://task-manager-chi-roan.vercel.app  
API Docs: https://task-manager-api-tt8l.onrender.com/docs 
---

## Features

- User signup and login using JWT authentication  
- Secure password hashing  
- Create, view, complete, and delete tasks  
- Each user can access only their own tasks (proper authorization)  
- Lightweight frontend for interacting with the API  

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite  
- **Authentication:** JWT (python-jose), Passlib  
- **Frontend:** HTML, CSS, JavaScript  

---

## How to Run Locally

### 1. Install dependencies

pip install -r requirements.txt

## 2. Run the backend server
uvicorn app.main:app --reload

## 3. Open API documentation

http://127.0.0.1:8000/docs

## 4. Run the frontend
cd frontend
python -m http.server 5500

## 5. Open in browser

http://localhost:5500

### API Endpoints:
POST /auth/signup → Register a new user

POST /auth/login → Login and receive access token

GET /tasks/ → Get all tasks for the logged-in user

POST /tasks/ → Create a new task

PUT /tasks/{id}/complete → Mark a task as completed

DELETE /tasks/{id} → Delete a task

## Notes:
The authentication token is passed as a query parameter for simplicity.

The focus of this project is on backend functionality and correctness rather than production-level deployment.

The frontend is intentionally kept simple to demonstrate API usage clearly.

The backend is hosted on Render (free tier), so the first request may take a few seconds due to cold start.

## What I Focused On:
While building this project, I focused on:

Keeping the code simple and readable

Implementing proper authentication and authorization

Ensuring users cannot access other users' data

Debugging frontend-backend integration issues carefully

## Future Improvements:
If extended further, I would:

Use Authorization headers instead of query parameters for tokens

Add pagination and filtering for tasks

Improve UI using a frontend framework like React

Deploy using Docker for better scalability
