import openai
import tiktoken
import time
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

COMPLETIONS_MODEL = "gpt4"

def num_tokens_from_string(string: str, encoding_name = COMPLETIONS_MODEL) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def openai_model(content, question):
    messages = [{"role":"system","content": f"You are a proficient problem solver, Expertise in finding the answer to the given context information, organizing the answer appropriately, and extracting the key points from the given context information.Reply your answer in mardkown format.Make sure your answer is right!"}]
    messages.append({"role":"user", "content": f"Given the context information and not prior knowledge\nAnswer the question : {question}\n### context information:\n{content}\n### answer: "})
    num_token = num_tokens_from_string(messages[0]["content"] + messages[1]["content"])
    print("total token spend for prompt :" ,num_token)

    while True:
        try : 
            response = openai.ChatCompletion.create(
                            model = COMPLETIONS_MODEL,
                            messages = messages,
                            temperature = 0.8,
                            max_tokens = 2000
                        )
            break
        except Exception as err:
            print(err)
            time.sleep(0.1)
    answer = response.choices[0].message['content']
    return answer