import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser
from gemini_api import ask_gemini

# Initialize the speech engine using gTTS as fallback for macOS to avoid pyttsx3 issues
from gtts import gTTS
import tempfile
import subprocess

def speak(text):
    print("JARVIS:", text)
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            subprocess.run(["afplay", fp.name])
    except Exception as e:
        print(f"Error in speak: {e}")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.WaitTimeoutError:
            speak("Listening timed out, please try again.")
            return ""
        except Exception as e:
            speak(f"An error occurred: {e}")
            return ""

def run_assistant():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        command = listen()
        if command == "":
            continue

        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Boss, playing {song} on YouTube")
            try:
                pywhatkit.playonyt(song)
            except Exception:
                speak("YouTube playback failed, checking other platforms as well.")
                # Open Spotify web player search
                spotify_url = f"https://open.spotify.com/search/{song.replace(' ', '%20')}"
                speak(f"Boss, checking Spotify for {song}")
                webbrowser.open(spotify_url)
                # Open Apple Music web player search
                apple_music_url = f"https://music.apple.com/search?term={song.replace(' ', '+')}"
                speak(f"Boss, checking Apple Music for {song}")
                webbrowser.open(apple_music_url)
                # Open Amazon Music web player search
                amazon_music_url = f"https://music.amazon.com/search/{song.replace(' ', '%20')}"
                speak(f"Boss, checking Amazon Music for {song}")
                webbrowser.open(amazon_music_url)

        elif 'time' in command:
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {now}")

        elif 'who is' in command or 'what is' in command:
            topic = command.replace('who is', '').replace('what is', '').strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for that topic, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I could not find any information on that topic.")
            except Exception as e:
                speak(f"An error occurred while searching Wikipedia: {e}")

        elif 'tell me a joke' in command:
            joke = ask_gemini("Tell me a joke")
            speak(joke)

        elif 'summarize this' in command:
            speak("Please provide the text to summarize.")
            text_to_summarize = listen()
            if text_to_summarize:
                summary = ask_gemini(f"Summarize this: {text_to_summarize}")
                speak(summary)
            else:
                speak("No text provided for summarization.")

        elif 'check the weather' in command:
            speak("Weather checking feature is not implemented yet.")

        elif 'open my email' in command:
            speak("Email opening feature is not implemented yet.")

        elif 'open' in command:
            app = command.replace('open', '').strip()
            if app in ['youtube', 'google', 'gmail', 'email']:
                url_map = {
                    'youtube': 'https://www.youtube.com',
                    'google': 'https://www.google.com',
                    'gmail': 'https://mail.google.com',
                    'email': 'https://mail.google.com',
                }
                url = url_map.get(app, None)
                if url:
                    speak(f"Opening {app}")
                    webbrowser.open(url)
                else:
                    speak(f"Sorry, I don't know how to open {app}")
            else:
                speak(f"Opening {app}")
                os.system(f"open -a '{app}'")

        elif 'shutdown' in command:
            speak("Shutting down. Goodbye!")
            break

        elif 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I can't perform that command yet.")

if __name__ == "__main__":
    run_assistant()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.WaitTimeoutError:
            speak("Listening timed out, please try again.")
            return ""
        except Exception as e:
            speak(f"An error occurred: {e}")
            return ""

def run_assistant():
    speak("Hello, I am your  personal assistant. How can I help you today chandu?")
    while True:
        command = listen()
        if command == "":
            continue

        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {now}")

        elif 'who is' in command or 'what is' in command:
            topic = command.replace('who is', '').replace('what is', '').strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for that topic, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I could not find any information on that topic.")
            except Exception as e:
                speak(f"An error occurred while searching Wikipedia: {e}")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'open' in command:
            app = command.replace('open', '').strip()
            speak(f"Opening {app}")
            # Simple example for macOS, can be extended for other apps or OS
            os.system(f"open -a '{app}'")

        elif 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I can't perform that command yet.")

if __name__ == "__main__":
    run_assistant()
