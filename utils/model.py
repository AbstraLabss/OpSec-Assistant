import tiktoken
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_APIKEY")
client = OpenAI()

COMPLETIONS_MODEL = "gpt-3.5-turbo"

def num_tokens_from_string(string: str, encoding_name = COMPLETIONS_MODEL) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def generate_respond(content:str, question:str):
    input_messages = [
            {"role": "system", "content": "You are a helpful assistant, given Content below, please answer the Question. If you don't know the answer. Just reply 'I don't know.'\n"},
            {"role": "user", "content": f"Content: {content}\nQuestion:{question}\nAnswer:"}
        ]
    num_token = num_tokens_from_string(input_messages[0]["content"] + input_messages[1]["content"])
    print("total token spend for prompt :" ,num_token)
    
    response = client.chat.completions.create(
        model=COMPLETIONS_MODEL,
        messages=input_messages
    )
    return response.choices[0].message.content
    