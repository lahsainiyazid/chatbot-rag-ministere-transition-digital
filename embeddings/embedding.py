import json
import numpy as np 
from sentence_transformers import SentenceTransformer 
model=SentenceTransformer("all-MiniLM-L6-v2")
with open("/home/yazid/rag/chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
text=[chunk["content"] for chunk in chunks]
embeddings=model.encode(text,show_progress_bar=True)
print(embeddings.shape)
np.save("services_embeddings.npy",embeddings)
