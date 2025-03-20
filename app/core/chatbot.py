from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.embedding import PineconeIntegration
from app.models.db_models import ChatbotData

pinecone_client = PineconeIntegration()

async def get_chatbot_response(user_input: str, db: AsyncSession):
    # Cari jawaban di Pinecone
    pinecone_results = pinecone_client.query_embedding(user_input, top_k=1)
    if pinecone_results.matches:
        return pinecone_results.matches[0].metadata["answer"]  # Kembalikan jawaban dari Pinecone
    
    # Jika tidak ditemukan di Pinecone, cari di database PostgreSQL
    result = await db.execute(select(ChatbotData.answer).where(ChatbotData.question == user_input))
    qa_pair = result.scalar()
    
    if qa_pair:
        # Simpan ke Pinecone untuk pencarian di masa depan
        pinecone_client.upsert_embedding(str(qa_pair.id), user_input, qa_pair.answer)
        return qa_pair  # Kembalikan jawaban dari database
    
    # Jika tidak ditemukan, gunakan GROQ API
    from app.core.groq_integration import query_groq_llama
    response = await query_groq_llama(user_input)
    return response