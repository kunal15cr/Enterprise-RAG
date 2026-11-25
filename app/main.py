from fastapi import FastAPI

from app.api import auth, admin

app = FastAPI(title="ADV RAG", version="0.1.0")
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
