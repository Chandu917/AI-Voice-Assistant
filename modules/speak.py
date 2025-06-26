import os
import speech_recognition as sr
from gtts import gTTS
import tempfile
import subprocess

def speak(text):
    print(f"Jarvis: {text}")
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            # Use afplay on macOS to play audio
            subprocess.run(["afplay", fp.name])
    except Exception as e:
        print(f"Error in speak: {e}")

def listen(timeout=10, phrase_time_limit=15, retries=3):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000  # Adjust based on mic sensitivity
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=2.0)
        for attempt in range(retries):
            try:
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.WaitTimeoutError:
                speak("I didn't hear anything.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't understand.")
            except sr.RequestError:
                speak("Speech service is unavailable.")
            except Exception as e:
                speak(f"Error occurred: {e}")
        return ""
