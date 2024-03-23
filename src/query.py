import logging
import os
import re
from langchain.vectorstores import Chroma
from utils import openai_model
from constants import (
    EMBEDDING_MODEL_NAME,
    EMBEDDING_DIRECTORY
)

def query_prompt(question:str):
    db = Chroma(
            persist_directory = EMBEDDING_DIRECTORY,
            embedding_function = EMBEDDING_MODEL_NAME
        )

    # answer question
    docs = db.similarity_search_with_score(question, k = 2)

    content = ""

    for doc in docs:
        content = content + doc[0].page_content
        print("\n\nContent can be found in : ", doc[0].metadata)
        print("\n\n\n")

    prompt = f"Given the context information and not prior knowledge\nAnswer the question : {question}\n### context information:\n{content}\n### answer: "
    return prompt