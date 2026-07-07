from sentence_transformers import SentenceTransformer 
import json
model=SentenceTransformer("all-MiniLM-L6-v2")
with open("/home/yazid/rag/v2/scrape/scraped/data.json","r",encoding="utf-8") as f:
    docs=json.load(f)

texts=[]
for doc in docs:
    texts.append(doc["content"])
embeddings=model.encode(texts)
print(len(embeddings))
