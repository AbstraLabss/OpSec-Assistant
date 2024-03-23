import logging
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import pandas as pd
import re
from langchain.docstore.document import Document
from langchain.text_splitter import Language, RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import chromadb
from chromadb.config import Settings

from constants import (
    EMBEDDING_MODEL_NAME,
    INGEST_THREADS,
    EMBEDDING_DIRECTORY,
    SOURCE_DIRECTORY
)

def main():
    df = pd.read_csv("Starknet_docs.csv", encoding = "utf-8")
    logging.info(f"Loading documents from {SOURCE_DIRECTORY}")
    
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size = 500,
        chunk_overlap  = 50,
        length_function = len,
        is_separator_regex = False,
    )

    # change to langchain format
    metadatas = []
    for i in list(df["url"]):
        metadatas.append({"document":i})

    texts = text_splitter.create_documents(list(df["content"]), metadatas=metadatas)
    logging.info(f"Split into {len(texts)} chunks of text")

    # save into chromadb
    # client = chromadb.PersistentClient(settings=CHROMA_SETTINGS , path=EMBEDDING_DIRECTORY)
    db = Chroma.from_documents(
        texts,
        EMBEDDING_MODEL_NAME,
        persist_directory=EMBEDDING_DIRECTORY,
    )

    logging.info(f"Save to database :{EMBEDDING_DIRECTORY}")


if __name__ == "__main__":

    main()