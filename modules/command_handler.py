import subprocess
import os
import re
try:
    from modules.gemini_api import ask_gemini
except ImportError:
    from modules.mock_gemini_api import ask_gemini

def open_app(app_name):
    apps = {
        "brave": "/Applications/Brave Browser.app",
        "finder": "/System/Library/CoreServices/Finder.app",
        "spotify": "/Applications/Spotify.app",
    }
    app_path = apps.get(app_name.lower())
    if app_path:
        if os.path.exists(app_path):
            subprocess.Popen(["open", app_path])
            return True
        else:
            print(f"The file {app_path} does not exist.")
            return False
    else:
        print(f"App path for {app_name} not found.")
        return False

def open_website_in_brave(url):
    brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    try:
        print(f"Opening Brave with URL: {url}")
        subprocess.Popen([brave_path, "--new-window", url])
        return True
    except Exception as e:
        print(f"Error opening Brave: {e}")
        return False

def handle_command(command):
    command = command.lower()

    # Direct command handling for common commands to avoid Gemini parsing issues
    if "open youtube" in command or "go to youtube" in command:
        import webbrowser
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "open google" in command:
        import webbrowser
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "open spotify" in command:
        import webbrowser
        webbrowser.open("https://open.spotify.com")
        return "Opening Spotify."
    elif "open netflix" in command:
        import webbrowser
        webbrowser.open("https://www.netflix.com")
        return "Opening Netflix."
    elif "open twitter" in command:
        import webbrowser
        webbrowser.open("https://www.twitter.com")
        return "Opening Twitter."
    elif "open github" in command:
        import webbrowser
        webbrowser.open("https://www.github.com")
        return "Opening GitHub."
    elif "shutdown" in command:
        return "Shutting down."
    else:
        # Use Gemini API to parse intent
        prompt = f"Parse the following command and respond with the intent and target in JSON format. Command: \"{command}\""
        response_text = ask_gemini(prompt)
        # Expected response example: {"intent": "open_website", "target": "youtube"}
        try:
            import json
            response_json = json.loads(response_text)
            intent = response_json.get("intent")
            target = response_json.get("target")
        except Exception:
            intent = None
            target = None

        if intent == "open_app":
            if open_app(target):
                return f"Opening {target}."
            else:
                return f"Failed to open app: {target}."
        elif intent == "open_website":
            websites = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "netflix": "https://www.netflix.com",
                "twitter": "https://www.twitter.com",
                "github": "https://www.github.com",
                "spotify": "https://open.spotify.com",
            }
            url = websites.get(target)
            if url:
                if open_website_in_brave(url):
                    return f"Opening {target} in Brave."
                else:
                    return f"Failed to open {target} in Brave."
            else:
                return f"Unknown website target: {target}."
        elif intent == "shutdown":
            return "Shutting down."
        else:
            return "Command not recognized."
