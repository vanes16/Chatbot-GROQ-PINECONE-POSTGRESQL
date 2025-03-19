# GROQ-POSTGRESQL-PINECONE-Chatbot

GOD MODE

1️⃣ User Input ├─> Pengguna mengetik pertanyaan ke chatbot ↓

2️⃣ Cek di PostgreSQL (Database Utama) ├─> Lanjut ke Pinecone ❌ ↓

3️⃣ Cek di Pinecone (Vector Embedding) ├─> Cari pertanyaan serupa menggunakan vektor Embedding Open AI (atau yang lain) ├─> Jika ditemukan pertanyaan serupa → Ambil & kirim jawaban dari DB ✅ ├─> Jika ada referensi → Berikan ke Groq sebagai konteks ✅ ├─> Jika tidak ada → Lanjut ke Groq tanpa konteks ❌ ↓

4️⃣ Groq API (Llama Model) ├─> Model Llama menganalisis & menghasilkan jawaban ├─> (Optional) Simpan jawaban ke PostgreSQL untuk pertanyaan yang baru ↓

5️⃣ Output ke User ├─> Jawaban dikirim kembali ke pengguna ├─> (Optional) Sistem belajar dari input untuk memperkaya database
