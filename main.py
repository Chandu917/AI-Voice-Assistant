import os
import time
import logging
import speech_recognition as sr
# Removed pyttsx3 import and usage due to macOS pyobjc dependency issues with pyttsx3
# Using gTTS and afplay in modules/speak.py for TTS instead
from dotenv import load_dotenv
from modules.gemini_api import ask_gemini

# =========================
# Load API Key from .env
# =========================
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY not found in .env file")
    exit(1)

# =========================
# Setup logging
# =========================
LOG_FILE = "logs/jarvis.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# =========================
# Configuration constants
# =========================
WAKE_WORD = "hey jarvis"
WAKE_WORD_TIMEOUT = 10
COMMAND_TIMEOUT = 8
MAX_RETRIES = 3
SPEECH_RATE = 150
CHAT_HISTORY_FILE = "logs/chat_history.json"
MAX_CHAT_HISTORY = 10

# =========================
# Initialize speech modules
# =========================
recognizer = sr.Recognizer()
recognizer.energy_threshold = 3000  # Adjust based on your mic sensitivity

# Removed pyttsx3 TTS engine usage due to macOS pyobjc issues
# Using speak() from modules.speak.py instead

# =========================
# Text-to-Speech Function
# =========================
from modules.speak import speak

# =========================
# Speech-to-Text Function
# =========================
def listen(timeout=7, phrase_time_limit=15, retries=3):
    recognizer.energy_threshold = 3000
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=2.0)
        for attempt in range(retries):
            try:
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                logging.info(f"Recognized speech: {command}")
                return command
            except sr.WaitTimeoutError:
                speak("I didn't hear anything.")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand.")
            except sr.RequestError:
                speak("Network error. Please check your internet.")
            except Exception as e:
                speak(f"Error occurred: {e}")
        return ""

# =========================
# Chat History Management
# =========================
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        try:
            import json
            with open(CHAT_HISTORY_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Failed to load chat history: {e}")
    return []

def save_chat_history(history):
    try:
        import json
        with open(CHAT_HISTORY_FILE, "w") as f:
            json.dump(history[-MAX_CHAT_HISTORY:], f)
    except Exception as e:
        logging.error(f"Failed to save chat history: {e}")

# =========================
# Main JARVIS Loop
# =========================
def jarvis():
    speak("Jarvis is now online. Waiting for wake word...")

    try:
        retry_count = 0
        max_retries = MAX_RETRIES
        while True:
            with sr.Microphone() as source:
                print("Waiting for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                try:
                    audio = recognizer.listen(source, timeout=WAKE_WORD_TIMEOUT, phrase_time_limit=5)
                    trigger = recognizer.recognize_google(audio).lower()
                    logging.info(f"Wake word detected: {trigger}")
                    if WAKE_WORD in trigger:
                        speak("Yes boss, I am your assistant. Please authenticate yourself.")
                        # Authentication step
                        from modules.auth import authenticate
                        if not authenticate():
                            speak("Authentication failed. Please try again.")
                            continue
                        speak("Authentication successful. How can I help you?")
                        retry_count = 0
                        while True:
                            command = listen(timeout=COMMAND_TIMEOUT)
                            if not command or len(command) < 3:
                                speak("I didn't catch that clearly. Could you please repeat?")
                                retry_count += 1
                                if retry_count >= max_retries:
                                    speak("Too many failed attempts. Returning to standby.")
                                    break
                                continue
                            if any(word in command for word in ["shutdown", "exit", "quit"]):
                                speak("Shutting down. Goodbye.")
                                logging.info("Shutdown command received. Exiting.")
                                return
                            if "hey jarvis come back" in command:
                                speak("Returning focus to VS Code.")
                                import subprocess
                                subprocess.run(["osascript", "-e", 'tell application "Visual Studio Code" to activate'])
                                continue
                            # Confirmation before executing app or website commands
                            from modules.command_handler import handle_command
                            known_commands = ["open youtube", "open spotify", "open downloads", "open finder", "open mac settings", "go to youtube"]
                            if any(cmd in command for cmd in known_commands):
                                # Removed confirmation prompt to simplify command execution
                                response = handle_command(command)
                                if response:
                                    speak(response)
                                continue
                            else:
                                # Use Gemini AI to interpret and respond to other commands
                                response = ask_gemini(command)
                                if response:
                                    speak(response)
                                else:
                                    speak("Sorry, I couldn't understand.")
                                retry_count = 0
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    continue
                except sr.RequestError:
                    speak("Network issue. Cannot process.")
                    logging.error("Network issue during wake word detection.")
                    continue
    except Exception as e:
        import traceback
        logging.error(f"Unexpected error in main loop: {e}")
        traceback.print_exc()
        speak("An unexpected error occurred. Shutting down.")
    finally:
        cleanup()

def cleanup():
    speak("Jarvis shutdown complete.")
    print("Jarvis has been shut down.")
    logging.info("Jarvis shutdown complete.")

if __name__ == "__main__":
    jarvis()
