from openai import OpenAI
import openai
import tiktoken
import time
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

COMPLETIONS_MODEL = "gpt-4"


def num_tokens_from_string(string: str, encoding_name = COMPLETIONS_MODEL) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def openai_model(content, question):

    client = OpenAI()

    while True:
        try : 
            response = client.chat.completions.create(
            model=COMPLETIONS_MODEL,
            messages=[
                {"role": "system", "content": "You are a proficient problem solver, Expertise in finding the answer to the given context information, organizing the answer appropriately, and extracting the key points from the given context information. Reply your answer in mardkown format.Make sure your answer is right!"},
                {"role": "user", "content": f"Given the context information and not prior knowledge\nAnswer the question : {question}\n### context information:\n{content}\n### answer: "}
            ],
            max_tokens = 3000
            )
            break
        except Exception as err:
            print(err)
            time.sleep(0.1)

    answer = response.choices[0].message.content
    return answer