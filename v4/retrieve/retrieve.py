import json 
import os 
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from google import genai 
with open ("/home/yazid/rag/v4/chunks/chunks-copy.json","r",encoding="utf-8") as f:
    chunks=json.load(f)
documents=[]
for chunk in chunks:
    documents.append(Document(page_content=chunk["text"],
                              metadata={
                              "titre":chunk["metadata"]["titre"],
                              "url":chunk["metadata"]["url"], 
                              "sous_rubrique":chunk["metadata"]["sous_rubrique"],
                              "rubrique":chunk["metadata"]["rubrique"],
                              "rubrique_principale":chunk["metadata"]["rubrique_principale"],
                              "chunk_id":chunk["metadata"]["chunk_id"]}))
bm25=BM25Retriever.from_documents(documents)
Question=input("Entrez votre question:")
bm25.k=5 
docs=bm25.invoke(Question)
context="\n\n".join(doc.page_content for doc in docs)
prompt=f"""Tu es un assistant gouvernemental reponds de maniere concise en utilisant le contexte:
contexte:{context}
question:{Question}
"""
key=os.environ.get("key")
client=genai.Client(api_key=key)
response=client.models.generate_content(model="gemini-2.5-flash",
                                      contents=prompt)
print(response.text)
