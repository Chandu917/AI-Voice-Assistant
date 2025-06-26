import os
import sys
import time
import threading
import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY not set in environment variables.")
    sys.exit(1)

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Constants
WAKE_WORD = "hey jarvis"
PASS_PHRASE = "i am your boss"
MAX_RETRIES = 2
SHUTDOWN_COMMANDS = ["exit", "shutdown", "stop listening", "quit", "bye"]

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speech rate
engine.setProperty('volume', 1.0)  # Volume 0-1

# Select voice (male or female)
voices = engine.getProperty('voices')
# Default to female voice if available
female_voice = next((v for v in voices if "female" in v.name.lower()), None)
if female_voice:
    engine.setProperty('voice', female_voice.id)
else:
    # fallback to first voice
    engine.setProperty('voice', voices[0].id)

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

def query_openai(prompt):
    """Query OpenAI GPT for a response"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None,
        )
        return response.choices[0].text.strip()
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
        # Query OpenAI for general questions or conversation
        speak("Let me think...")
        response = query_openai(command)
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
