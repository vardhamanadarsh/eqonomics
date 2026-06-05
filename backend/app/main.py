from fastapi import FastAPI

app = FastAPI(
    title="Eqonomics API",
    description="Backend API for Eqonomics",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Eqonomics API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }