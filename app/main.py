from fastapi import FastAPI
from app.routers import upload, navigation

app = FastAPI()

# Include routers
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(navigation.router, prefix="/api", tags=["Navigation"])

@app.get("/api/health/")
def read_root():
    return {"message": "Backend is running!"}
