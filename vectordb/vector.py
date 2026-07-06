import json
import numpy as np 
import faiss
from sentence_transformers import SentenceTransformer 
model=SentenceTransformer("all-MiniLM-L6-v2")
with open ("/home/yazid/rag/chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
texts=[chunk["content"] for chunk in chunks ]
embeddings=model.encode(texts,show_progress_bar=True)
embeddings=np.array(embeddings).astype("float32")
dim=embeddings.shape[1]
index=faiss.IndexFlatL2(dim)
index.add(embeddings)
faiss.write_index(index,"vector_services.index") 

