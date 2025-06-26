from modules.speak import speak, listen

PASS_PHRASE = "i am your boss"
MAX_RETRIES = 3

def authenticate():
    # Removed authentication prompt as per user request
    for _ in range(MAX_RETRIES):
        phrase = listen()
        if phrase == PASS_PHRASE:
            speak("Authentication successful. Welcome back, boss.")
            return True
        else:
            speak("Incorrect passphrase.")
    speak("Access denied.")
    return False
