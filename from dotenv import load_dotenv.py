from dotenv import load_dotenv
import os
load_dotenv()
access_key = os.getenv('PORCUPINE_ACCESS_KEY')
if not access_key:
    print("❌ Access key not found")
    exit(1)
print("✅ Access Key Loaded:", access_key[:8] + "..." + access_key[-4:])