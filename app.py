import streamlit as st
import os
from streamlit_chat import message
from qdrant_client import QdrantClient
from utils.constant import COLLECTION_NAME, EMBEDDING_MODEL
from utils.model import generate_respond
from functools import lru_cache
from embedding import get_embedding
from dotenv import load_dotenv
load_dotenv()

@lru_cache(maxsize=None)
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

def get_text():
	input_text = st.text_input("Please ask me anything about OpSec.", key="input")
	return input_text

def main():

	st.title("OpSec Assistant")

	if 'user_input' not in st.session_state:
		st.session_state['user_input'] = []

	if 'assistant_response' not in st.session_state:
		st.session_state['assistant_response'] = []

	user_input = get_text()

	if user_input:
		qclient = get_client()
		query_embedding = get_embedding(user_input, EMBEDDING_MODEL)
		results = search_from_qdrant(qclient, query_embedding, k=4)
        
		need_info = ""
		for result in results:
			need_info += result.payload["content"]
			need_info += "\n"
		
		print(need_info)
		answer = generate_respond(need_info, user_input)

		# Store the output
		st.session_state.assistant_response.append(user_input)
		st.session_state.user_input.append(answer)

	message_history = st.empty()

	if st.session_state['user_input']:
		for i in range(len(st.session_state['user_input']) - 1, -1, -1):
			# This function displays user input
			message(st.session_state["user_input"][i], 
					key=str(i),avatar_style="icons")
			# This function displays OpenAI response
			message(st.session_state['assistant_response'][i], 
					avatar_style="miniavs",is_user=True,
					key=str(i) + 'data_by_user')

if __name__ == "__main__":
    main()