from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import auth_routes, task_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Task Management API is running"}

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])