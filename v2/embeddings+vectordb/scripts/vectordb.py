from langchain_core.documents import Document 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS
import json 
with open("/home/yazid/rag/v2/chunking/chunks/chunks.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
docs=[]
for chunk in chunks:
    docs.append(Document(page_content=chunk["text"],
                         metadata={"titre":chunk["metadata"]["titre"],
                                    "url":chunk["metadata"]["url"],
                                    "sous_rubrique":chunk["metadata"]["sous_rubrique"],
                                    "rubrique":chunk["metadata"]["rubrique"],
                                    "rubrique_principale":chunk["metadata"]["rubrique_principale"],
                                    "chunk_id":chunk["metadata"]["chunk_id"]}))

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
db=FAISS.from_documents(docs,embeddings)
db.save_local("faiss_db")
