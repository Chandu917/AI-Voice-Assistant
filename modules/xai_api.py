import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('XAI_API_KEY')
if not api_key:
    print("ERROR: No XAI_API_KEY found in .env!")
    exit(1)

def ask_xai(prompt):
    try:
        url = "https://api.x.ai/grok"  # Confirmed xAI endpoint without /v1
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "model": "grok-3"
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_response = response.json()
        # Improved response parsing to handle different possible structures
        if isinstance(json_response, dict):
            if 'choices' in json_response and len(json_response['choices']) > 0:
                return json_response['choices'][0].get('text', '').strip()
            elif 'text' in json_response:
                return json_response['text'].strip()
            elif 'response' in json_response:
                return str(json_response['response']).strip()
        return "Received unexpected response format from xAI."
    except requests.exceptions.ConnectionError:
        return "Sorry, I could not contact xAI right now."
    except requests.exceptions.HTTPError as e:
        return f"xAI API error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
