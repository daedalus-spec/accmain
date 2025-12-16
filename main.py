from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake database (in-memory)
users_db = {
    "john": {
        "username": "john",
        "password": "1234",
        "account_number": "ACC1001",
        "balance": 5000.75
    },
    "alice": {
        "username": "alice",
        "password": "abcd",
        "account_number": "ACC1002",
        "balance": 12000.00
    }
}

# --------- Models ---------

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    message: str
    username: str

# --------- Routes ---------

@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    user = users_db.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "username": user["username"]
    }

@app.get("/account/{username}")
def get_account_details(username: str):
    user = users_db.get(username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user["username"],
        "account_number": user["account_number"],
        "password": user["password"],   # plaintext as requested
        "balance": user["balance"]
    }
