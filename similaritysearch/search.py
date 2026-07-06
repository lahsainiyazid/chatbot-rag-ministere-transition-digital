from sentence_transformers import SentenceTransformer 
import faiss 
import json 
model=SentenceTransformer("all-MiniLM-L6-v2")
index=faiss.read_index("/home/yazid/rag/vectordb/vector_services.index")
with open ("/home/yazid/rag/chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
question=input("Entrez votre question:")
query_embedding=model.encode([question])
k=3
distances,indices=index.search(query_embedding,k)
for i in indices[0]:
    print(chunks[i])
