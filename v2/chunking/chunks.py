import json
from langchain_text_splitters import RecursiveCharacterTextSplitter 
with open("/home/yazid/rag/v2/scrape/scraped/full-services.json","r",encoding="utf-8") as f:
    data=json.load(f)
splitter=RecursiveCharacterTextSplitter(chunk_size=500,
                                         chunk_overlap=100)
chunks=[]
for doc in data:
    text_chunks=splitter.split_text(doc["content"])
    for i,chunk in enumerate(text_chunks):
        chunks.append({"text":chunk,
                       "metadata":{"titre":doc["titre"],
                       "url":doc["url"],
                        "sous_rubrique":doc["sous_rubrique"],
                         "rubrique":doc["rubrique"],
                          "rubrique_principale":doc["rubrique_principale"],
                       "chunk_id":i}})

with open("chunks.json","w",encoding="utf-8") as f:
    json.dump(chunks,f,ensure_ascii=False,indent=4)

