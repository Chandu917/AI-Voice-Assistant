import subprocess

def speak(text):
    # Use macOS native 'say' command with Samantha voice for sweet female voice
    subprocess.run(['say', '-v', 'Samantha', text])
