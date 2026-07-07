from sentence_transformers import SentenceTransformer 
from google import genai 
import os 
import faiss 
import json
key=os.environ.get("key")
client=genai.Client(api_key=key)
def charger_prompt(chemin="prompt.txt"):
    with open(chemin,"r",encoding="utf-8") as f:
        return f.read()
prompt=charger_prompt()
question=input("Entrez votre question:")
model=SentenceTransformer("all-MiniLM-L6-v2")
index=faiss.read_index("/home/yazid/rag/vectordb/vector_services.index")
with open ("/home/yazid/rag/chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
query_embedding=model.encode([question])
k=3
distances,indices=index.search(query_embedding,k)
contexte_recupere="\n\n".join(chunks[i]["content"] for i in indices[0])
prompt_final=prompt.format(context=contexte_recupere,
query=question)
print(prompt_final)
response=client.models.generate_content(model="gemini-2.5-flash",
                                        contents=prompt_final)
print(response.text)
