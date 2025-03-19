from app.core.groq_integration import GroqIntegration

async def get_chatbot_response(user_input: str):
    """
    Mendapatkan respons dari chatbot menggunakan GROQ API.
    
    :param user_input: Input dari pengguna.
    :return: Respons dari chatbot.
    """
    try:
        # Inisialisasi Groq client
        groq_client = GroqIntegration()
        
        # Pilih model yang akan digunakan (misalnya, 'llama2-70b')
        model = "llama3-70b-8192"
        
        # Kirim input pengguna ke GROQ API
        response = groq_client.query_groq(model=model, prompt=user_input)
        
        # Kembalikan respons
        return response
    except Exception as e:
        print(f"Error in get_chatbot_response: {e}")
        return "Maaf, terjadi kesalahan saat memproses permintaan Anda."