from modules.speak import listen, speak
try:
    from modules.gemini_api import ask_gemini
except ImportError:
    from modules.mock_gemini_api import ask_gemini
from modules.command_handler import handle_command
import sys

def run_jarvis():
    try:
        print("Jarvis is listening for the wake word 'Hey Jarvis'.")
        command = listen(timeout=10, phrase_time_limit=15)
        print(f"DEBUG: Heard command: {command}")
        if not command:
            speak("I didn't hear anything. Please try again, boss.")
            return
        if "hey jarvis" in command.lower():
            speak("Yes boss, please confirm your identity with the passphrase.")
            passphrase = listen(timeout=10, phrase_time_limit=10)
            print(f"DEBUG: Heard passphrase: {passphrase}")
            if not passphrase:
                speak("I didn't hear the passphrase. Please try again, boss.")
                return
            if "i am your boss" in passphrase.lower():
                speak("Authentication successful, boss. How can I assist you?")
                while True:
                    actual_command = listen(timeout=15, phrase_time_limit=20)
                    print(f"DEBUG: Heard actual command: {actual_command}")
                    if not actual_command:
                        speak("No command detected. Is there anything else I can assist you with, boss?")
                        continue
                    if actual_command.lower() in ["exit", "shutdown", "goodbye", "quit"]:
                        speak("As you command, boss. Shutting down now. Goodbye, boss.")
                        break
                    print(f"Executing command: {actual_command}")
                    response = handle_command(actual_command)
                    speak("As you command, boss.")
                    speak(response)
                    speak("Is there anything else I can assist you with, boss?")
            else:
                speak("Authentication failed. Access denied, boss.")
        else:
            speak("Wake word not detected. Please try again, boss.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_jarvis()
