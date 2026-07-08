import os 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS 
from google import genai 
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
db=FAISS.load_local("/home/yazid/rag/v2/embeddings+vectordb/db/faiss_db",embeddings,allow_dangerous_deserialization=True)
question=input("Entrez votre question:")
docs=db.similarity_search(question,k=10)
key=os.environ.get("key")
content="\n\n".join(f"Titre:{doc.metadata.get('title')}\n"
                     f"Contenu:{doc.page_content}"
                     for doc in docs)
prompt=f"""Tu es un assistant administratif maroccain au ministere de la transition digitale Réponds uniquement avec les informations du contexte.
 Contexte:{content}
 Question:{question}
    """
client=genai.Client(api_key=key)
response=client.models.generate_content(model="gemini-2.5-flash",
                                        contents=prompt)
print(response.text)
