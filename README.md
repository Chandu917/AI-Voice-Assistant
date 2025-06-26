# Jarvis AI Assistant

## Overview

Jarvis is an advanced voice-based AI assistant inspired by Iron Man's Jarvis. It listens for a wake word, authenticates the user via a passphrase, and can perform a variety of tasks including opening websites, running system commands, and answering questions using OpenAI's GPT.

## Features

- Wake word detection ("Hey Jarvis")
- Voice authentication with passphrase ("I am your boss")
- Voice input and output using speech recognition and text-to-speech
- Integration with OpenAI GPT for conversational AI
- System command execution and website launching
- Graceful error handling and network checks
- Cross-platform compatibility (macOS, Windows, Linux)

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### Running Jarvis

Run the assistant with:

```bash
python3 jarvis.py
```

Jarvis will announce when it is online and start listening for the wake word.

## Commands Jarvis Can Understand

- "Hey Jarvis" (wake word)
- Passphrase: "I am your boss" (for authentication)
- Open websites: "open YouTube", "open GitHub", "open Netflix", "open Google", "open Twitter"
- Run system commands: "run [command]"
- Shutdown commands: "exit", "shutdown", "stop listening", "quit", "bye"
- General questions and conversation (via OpenAI GPT)

## Tips for Improvements and Debugging

- Adjust speech recognition timeout and phrase limits in `jarvis.py` for better responsiveness.
- Customize voice properties (rate, volume, voice) in the `speak` function.
- Add conversational memory by storing recent interactions.
- Implement offline fallback using local NLP models.
- Integrate additional APIs like Spotify, Google Calendar, or Weather.
- Use unit tests and mocks for microphone and speech recognition modules.
- Monitor logs for errors and performance issues.

## License

This project is open source and free to use.
