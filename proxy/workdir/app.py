import os
from flask import Flask, request
import openai

openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 256

app = Flask(__name__)

@app.route('/', methods=['POST'])
def send_request_chatgpt():
    json_data = request.get_json()
    print(json_data)
    completion = openai.ChatCompletion.create(
        model=MODEL,
        messages=json_data,
        max_tokens=MAX_TOKENS
    )

    return completion

if __name__ == '__main__':
    app.run(host='localhost', port=8000)