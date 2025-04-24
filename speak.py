import pyttsx3
import threading

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Adjust the speed of speech

stop_flag = False
callback_textbox = None
speaking_thread = None

def speak(text, update_callback=None):
    global stop_flag, callback_textbox, speaking_thread
    stop_flag = False
    callback_textbox = update_callback

    def run():
        global stop_flag
        if callback_textbox:
            callback_textbox(text)  # Display the text instantly
        if stop_flag:
            return
        # Speak the text directly after displaying
        engine.say(text)
        engine.runAndWait()

    # Create a new thread to avoid blocking the main GUI thread
    speaking_thread = threading.Thread(target=run)
    speaking_thread.start()

def stop_speaking():
    global stop_flag
    stop_flag = True
    try:
        engine.stop()  # This stops the speaking immediately
    except RuntimeError:
        pass  # If already stopped or other error
