import json
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_core.documents import Document
with open("./data/chatbot_data/services.json","r",encoding="utf-8") as f:
    documents =json.load(f)


text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
chunks=[]
for doc in documents:
    split_texts=text_splitter.split_text(doc["content"])
    for text in split_texts:
        chunks.append({
            "content":text,
            "url":doc["metadata"]["url"],
            "rubrique":doc["metadata"]["rubrique"]})

print(f"Created {len(chunks)} chunks ")
with open("chunks.json","w",encoding="utf-8") as f:
    json.dump(chunks,f,ensure_ascii=False,indent=4)
