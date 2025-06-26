import openai
import sys
sys.path.append("..")
from settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception:
        return "Sorry, I could not contact OpenAI right now."
