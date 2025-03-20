from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import init_db, get_db
from app.core.chatbot import get_chatbot_response
from app.models.db_models import ChatHistory
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Chatbot API is running!"}

@app.post("/chat")
async def chat(user_input: str, db: AsyncSession = Depends(get_db)):
    response = await get_chatbot_response(user_input)
    chat_history = ChatHistory(user_input=user_input, bot_response=response)
    
    db.add(chat_history)
    await db.commit()
    await db.refresh(chat_history)
    
    return {"response": response}

