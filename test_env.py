import os
from dotenv import load_dotenv

print("🔍 Loading .env file...")
load_dotenv()

print("📁 Current directory:", os.getcwd())

access_key = os.getenv("PORCUPINE_ACCESS_KEY")
if access_key:
    print(f"✅ Access key loaded: {access_key[:4]}...{access_key[-4:]}")
else:
    print("❌ Access key NOT loaded. Value is None")
