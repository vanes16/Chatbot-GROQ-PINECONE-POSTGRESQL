from fastapi import FastAPI
from app.core.chatbot import get_chatbot_response

app = FastAPI()

@app.post("/chat")
async def chat(user_input: str):
    response = await get_chatbot_response(user_input)
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Chatbot API is running!"}