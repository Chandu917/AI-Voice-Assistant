import os
import sys
import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not set in environment variables.")
    sys.exit(1)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini Pro Model
model = genai.GenerativeModel('gemini-pro')

# Constants
WAKE_WORD = "hey jarvis"
PASS_PHRASE = "i am your boss"
MAX_RETRIES = 2
SHUTDOWN_COMMANDS = ["exit", "shutdown", "stop listening", "quit", "bye"]

# Initialize speech engine
engine = pyttsx3.init()

# Improved voice selection and settings for better quality
voices = engine.getProperty('voices')
# Print available voices for debugging (can be commented out)
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")

# Select a preferred voice index (change as needed)
preferred_voice_index = 1 if len(voices) > 1 else 0
engine.setProperty('voice', voices[preferred_voice_index].id)

# Adjust speed and volume for clarity
engine.setProperty('rate', 170)  # Slightly slower for better clarity
engine.setProperty('volume', 1.0)  # Max volume

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    """Speak text using pyttsx3"""
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=10):
    """Listen to microphone and return recognized text"""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1.0)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            command = recognizer.recognize_google(audio, language="en-US").lower()
            return command
        except sr.WaitTimeoutError:
            speak("I didn't catch that, boss. Please say it again.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""

def open_website(url):
    """Open a website in the default browser"""
    webbrowser.open(url)

def run_command(command):
    """Run a system command"""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        speak(f"Failed to run command: {command}")

def authenticate():
    """Authenticate user by passphrase"""
    speak("Authentication required. Say the passphrase.")
    for _ in range(MAX_RETRIES):
        phrase = listen()
        if phrase == PASS_PHRASE:
            speak("Authentication successful. Welcome back, boss.")
            return True
        else:
            speak("Incorrect passphrase.")
    speak("Access denied.")
    return False

def query_gemini(prompt):
    """Query Google Gemini GPT for a response"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        speak("Sorry, I am having trouble connecting to the AI service.")
        return ""

def process_command(command):
    """Process user command"""
    if any(cmd in command for cmd in SHUTDOWN_COMMANDS):
        speak("Shutting down. Goodbye!")
        sys.exit(0)

    if "open youtube" in command:
        open_website("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open github" in command:
        open_website("https://github.com")
        speak("Opening GitHub.")
    elif "open netflix" in command:
        open_website("https://www.netflix.com")
        speak("Opening Netflix.")
    elif "open google" in command:
        open_website("https://www.google.com")
        speak("Opening Google.")
    elif "open twitter" in command:
        open_website("https://twitter.com")
        speak("Opening Twitter.")
    elif command.startswith("run "):
        cmd_to_run = command[4:]
        run_command(cmd_to_run)
        speak(f"Running command: {cmd_to_run}")
    else:
        # Query Gemini for general questions or conversation
        speak("Let me think...")
        response = query_gemini(command)
        if response:
            speak(response)
        else:
            speak("I couldn't get a response from the AI.")

def wait_for_wake_word():
    """Continuously listen for the wake word"""
    while True:
        print("Listening for wake word...")
        command = listen(timeout=None, phrase_time_limit=5)
        if WAKE_WORD in command:
            speak("Yes, boss?")
            if authenticate():
                speak("How can I assist you?")
                while True:
                    user_command = listen()
                    if user_command:
                        process_command(user_command)
                    else:
                        speak("Please say that again.")
            else:
                speak("Authentication failed. Returning to standby.")

def main():
    speak("Jarvis is now online.")
    wait_for_wake_word()

if __name__ == "__main__":
    main()
