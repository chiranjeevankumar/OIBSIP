import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Voice Assistant is listening. Speak now!")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            speak("The current time is " + datetime.datetime.now().strftime("%I:%M %p"))
        elif "date" in command or "today" in command:
            speak("Today's date is " + datetime.datetime.now().strftime("%d %B %Y"))
        elif "search" in command:
            query = command.replace("search", "", 1).strip()
            if query:
                speak("Searching the web for " + query)
                webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
            else:
                speak("Please tell me what you want to search for.")
        else:
            speak("Sorry, I don't understand that command. Please try again.")

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you. Please try again.")
    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
    except sr.RequestError:
        speak("The speech recognition service is unavailable.")
    except OSError:
        speak("A microphone is not available. Please check your microphone.")

if __name__ == "__main__":
    run_assistant()
