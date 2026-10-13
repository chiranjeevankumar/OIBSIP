
from google.colab.output import eval_js
from IPython.display import display, HTML
from datetime import datetime
from urllib.parse import quote_plus
import json


def speak(text):
    print("Assistant:", text)
    js_text = json.dumps(text)

    eval_js(f"""
        (() => {{
            window.speechSynthesis.cancel();
            const msg = new SpeechSynthesisUtterance({js_text});
            msg.lang = "en-IN";
            window.speechSynthesis.speak(msg);
            return true;
        }})()
    """)


def listen():
    return eval_js("""
        new Promise((resolve) => {
            const SR = window.SpeechRecognition ||
                       window.webkitSpeechRecognition;

            if (!SR) {
                resolve("__UNSUPPORTED__");
                return;
            }

            const recognition = new SR();
            recognition.lang = "en-IN";
            recognition.interimResults = false;

            recognition.onresult = (event) =>
                resolve(event.results[0][0].transcript);

            recognition.onerror = (event) =>
                resolve("__ERROR__:" + event.error);

            recognition.start();
        })
    """)


print("Android Voice Assistant is ready!")
print("Say hello, time, date, search Python, or exit.")

while True:
    command = listen()

    if command == "__UNSUPPORTED__":
        print("Speech recognition is not supported.")
        break

    if command.startswith("__ERROR__:"):
        print(command)
        continue

    command = command.lower().strip()
    print("You said:", command)

    if command in ("exit", "quit", "goodbye", "stop"):
        speak("Goodbye!")
        break

    elif "hello" in command or command == "hi":
        speak("Hello! How can I help you?")

    elif "time" in command:
        speak(
            "The current time is "
            + datetime.now().strftime("%I:%M %p")
        )

    elif "date" in command or "today" in command:
        speak(
            "Today's date is "
            + datetime.now().strftime("%d %B %Y")
        )

    elif "search" in command:
        query = command.replace("search", "", 1).strip()

        if query:
            speak("Searching the web for " + query)
            url = "https://www.google.com/search?q=" + quote_plus(query)

            display(HTML(
                f'<a href="{url}" target="_blank">'
                'Open Google search results</a>'
            ))
        else:
            speak("Please tell me what you want to search for.")

    else:
        speak("Sorry, I don't understand that command.")
