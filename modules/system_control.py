import subprocess

def execute_command(command):
    # Opening Finder
    if "open finder" in command:
        subprocess.run(["open", "/System/Library/CoreServices/Finder.app"])
        return "Opening Finder."

    # Opening Google Chrome
    elif "open chrome" in command:
        subprocess.run(["open", "-a", "Google Chrome"])
        return "Opening Google Chrome."

    # Opening Safari
    elif "open safari" in command:
        subprocess.run(["open", "-a", "Safari"])
        return "Opening Safari."

    # Opening Visual Studio Code
    elif "open vscode" in command or "open vs code" in command:
        subprocess.run(["open", "-a", "Visual Studio Code"])
        return "Opening Visual Studio Code."

    # Opening Spotify in Brave
    elif "open spotify" in command:
        subprocess.run(["open", "-a", "Brave Browser", "https://open.spotify.com"])
        return "Opening Spotify in Brave."

    # Opening YouTube in Brave
    elif "open youtube" in command:
        subprocess.run(["open", "-a", "Brave Browser", "https://youtube.com"])
        return "Opening YouTube in Brave."

    # Dynamic Website Opening in Brave
    elif "open" in command and "in brave" in command:
        try:
            website = command.replace("open", "").replace("in brave", "").strip()
            url = f"https://{website.lower().replace(' ', '')}.com"
            subprocess.run(["open", "-a", "Brave Browser", url])
            return f"Opening {website} in Brave."
        except Exception as e:
            return f"Failed to open {website} in Brave. Error: {e}"

    # Shutdown Command
    elif "shutdown" in command:
        return "Shutting down. Goodbye."

    else:
        return "Sorry boss, I did not understand that command."
