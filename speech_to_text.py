import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Waits a moment before considering speech done
        try:
            audio = r.listen(source, timeout=5)  # Waits max 5 seconds
            voice_data = r.recognize_google(audio, language="en-in")
            print("You said:", voice_data)
            return voice_data
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return "No speech detected"
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return "Could not understand"
        except sr.RequestError:
            print("Network error. Try again later.")
            return "Network error"
