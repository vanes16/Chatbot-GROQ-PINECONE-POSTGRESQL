from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = "chat_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String, nullable=False)
    bot_response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ChatbotData(Base):
    __tablename__ = "chatbot_data"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    additional_info = Column(JSONB, default={}) # Metadata opsional