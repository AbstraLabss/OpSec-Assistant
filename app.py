import streamlit as st
import openai
from streamlit_chat import message
from utils.utils import openai_model
from embedding import ask_db

st.title("OpSec Assistant")
st.title("Can answer anything about OpSec")

if 'user_input' not in st.session_state:
	st.session_state['user_input'] = []

if 'openai_response' not in st.session_state:
	st.session_state['openai_response'] = []

def get_text():
	input_text = st.text_input("Input your question about OpSec here", key="input")
	return input_text

user_input = get_text()

if user_input:
	information = ask_db(user_input)
	
	infor = information.lstrip("\n")
	answer = openai_model(infor, user_input)

	# Store the output
	st.session_state.openai_response.append(user_input)
	st.session_state.user_input.append(answer)

message_history = st.empty()

if st.session_state['user_input']:
	for i in range(len(st.session_state['user_input']) - 1, -1, -1):
		# This function displays user input
		message(st.session_state["user_input"][i], 
				key=str(i),avatar_style="icons")
		# This function displays OpenAI response
		message(st.session_state['openai_response'][i], 
				avatar_style="miniavs",is_user=True,
				key=str(i) + 'data_by_user')
