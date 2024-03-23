import os
#from chromadb.config import Settings
# https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/excel.html?highlight=xlsx#microsoft-excel
from langchain.document_loaders import CSVLoader, PDFMinerLoader, TextLoader, UnstructuredExcelLoader, UnstructuredWordDocumentLoader

import openai
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings


ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Define the folder for storing database
SOURCE_DIRECTORY = f"./dataset"

EMBEDDING_DIRECTORY = f"./Embedding"

# Can be changed to a specific number
INGEST_THREADS = os.cpu_count() or 8

# Define the Chroma settings 
# CHROMA_SETTINGS = Settings(
#     persist_directory=EMBEDDING_DIRECTORY, anonymized_telemetry=False
# )

# Define Search URL path
URL_PATH = ["https://docs.opsec.computer/",
            "https://docs.opsec.computer/category/getting-started",
            "https://docs.opsec.computer/category/opsec-cloudverse",
            "https://docs.opsec.computer/getting-started/opsec-cloudverse/opsec-nodes",
            "https://docs.opsec.computer/getting-started/opsec-cloudverse/opsec-vps",
            "https://docs.opsec.computer/getting-started/opsec-cloudverse/opsec-gpu",
            "https://docs.opsec.computer/category/opsec-network",
            "https://docs.opsec.computer/getting-started/opsec-network/core-features-of-opSec-network",
            "https://docs.opsec.computer/getting-started/opsec-network/core-functionalities",
            "https://docs.opsec.computer/getting-started/opsec-network/why-opsec",
            ]

### 
# Embedding model
###

EMBEDDING_MODEL_NAME = OpenAIEmbeddings(model = "text-embedding-3-large")


###
# Generation model
###