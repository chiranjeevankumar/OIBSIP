# Voice Assistant

## Project Overview
A Python voice assistant that recognizes spoken commands and responds using text-to-speech.

## Features
- Responds to Hello and Hi greetings.
- Announces the current time.
- Announces today's date.
- Searches the web using Google.
- Handles unrecognized speech and microphone errors.
- Uses speech recognition and text-to-speech.

## Technologies Used
- Python
- SpeechRecognition
- pyttsx3
- datetime
- webbrowser

## Installation
Install the required packages:

```bash
pip install SpeechRecognition pyttsx3
```

A working microphone and suitable audio support are required.

## Run the Project
```bash
python voice_assistant.py
```

## Note
This desktop version requires a local Python environment with microphone access and audio support. Google Colab uses a separate browser-based version.
