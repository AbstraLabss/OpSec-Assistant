from fastapi import FastAPI
from pydantic import BaseModel
import os
from qdrant_client import QdrantClient
from utils.constant import COLLECTION_NAME, EMBEDDING_MODEL
from utils.model import generate_respond
from embedding import get_embedding
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

class Query(BaseModel):
    query_text: str


def get_client():
    return QdrantClient(
        url=os.getenv("QDRANT_DB_URL"),
        api_key=os.getenv("QDRANT_APIKEY")
    )

def search_from_qdrant(client, vector, k):
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=k,
        append_payload=True,
    )
    return search_result

@app.post("/query/")
async def get_answer(query: Query):
    qclient = get_client()
    query_text = query.query_text

    query_embedding = get_embedding(query_text, EMBEDDING_MODEL)
    results = search_from_qdrant(qclient, query_embedding, k=6)

    need_info = ""
    for result in results:
        need_info += result.payload["content"]
        need_info += "\n"
    
    print(need_info)
    answer = generate_respond(need_info, query_text)
    return {"answer": answer}