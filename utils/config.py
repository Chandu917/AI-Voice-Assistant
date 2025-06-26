import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
WAKE_WORD = "hey jarvis"
PASS_PHRASE = "i am your boss"
BRAVE_PATH = "open -a 'Brave Browser'"
MAX_RETRIES = 2
LOG_FILE = "logs/jarvis_log.txt"
