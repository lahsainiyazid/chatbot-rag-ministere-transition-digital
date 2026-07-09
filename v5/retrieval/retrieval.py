import json 
import os 
from langchain_core.documents import Document 
from langchain_community.retrievers import BM25Retriever 
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import EnsembleRetriever 
from google import genai 
key=os.environ.get("key")
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
db=FAISS.load_local("/home/yazid/rag/v5/db/hybrid_db",embeddings,allow_dangerous_deserialization=True)
Question=input("Entrez votre question:")
dense_retriever=db.as_retriever(search_kwargs={"k":3})
with open("/home/yazid/rag/v5/chunks/hybrid-chunks.json","r",encoding="utf-8") as f :
    chunks=json.load(f)
documents=[]
for chunk in chunks:
    documents.append(Document(page_content=chunk["text"],
                              metadata={"titre":chunk["metadata"]["titre"],
                                        "url":chunk["metadata"]["url"],
                                        "sous_rubrique":chunk["metadata"]["sous_rubrique"],
                                        "rubrique":chunk["metadata"]["rubrique"],
                                        "rubrique_principale":chunk["metadata"]["rubrique_principale"],
                                        "chunk_id":chunk["metadata"]["chunk_id"]}))

bm25=BM25Retriever.from_documents(documents)
bm25.k=3
hybrid=EnsembleRetriever(retrievers=[bm25,dense_retriever],
                         weights=[0.8,0.2])
results=hybrid.invoke(Question)
context="\n\n".join(doc.page_content for doc in results)
prompt=f"""Tu es un assistant gouvernemental reponds de maniere concise en se basant sur ce contexte:
 Contexte:{context}
 Question:{Question}
    """
client=genai.Client(api_key=key)
response=client.models.generate_content(model="gemini-2.5-flash",
                                        contents=prompt)
print(response.text)
