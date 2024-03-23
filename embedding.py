# import
from langchain_community.document_loaders import TextLoader
import chromadb
from langchain_openai import OpenAIEmbeddings
import os
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
loader = TextLoader("information.txt")
documents = loader.load()

embeddings = OpenAIEmbeddings()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
# load it into Chroma
db = Chroma.from_documents(docs, embeddings)

def ask_db(query : str):

    query = query
    docs = db.similarity_search_with_score(query, k = 2)
    return_content = ""
    for doc in docs:
        return_content += doc[0].page_content
    print(return_content)
    return return_content
