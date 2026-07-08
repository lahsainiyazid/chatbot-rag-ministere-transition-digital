import os 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS 
from google import genai 
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
db=FAISS.load_local("/home/yazid/rag/v3/embeddings+vectordb/db/faiss_db",embeddings,allow_dangerous_deserialization=True)
Question=input("Entrez une question :")
results=db.similarity_search(Question,k=3)
context="\n\n".join(doc.page_content for doc in results)
prompt=f"""Tu es un assistant gouvernemental reponds uniquement a partir du contexte suivant:
 Contexte:{context}
 Question:{Question}
    """
key=os.environ.get("key")
client=genai.Client(api_key=key)
response=client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
print(response.text)
