import datetime
import speak
import webbrowser
import os
from local_model import chat_local

def Action(data, update_callback=None):   
    if not data:
        return "No input received."

    data_btn = data.lower()

    def speak_and_return(response):
        speak.speak(response, update_callback=update_callback)
        return response

    if "what is your name" in data_btn:
        return speak_and_return("My name is Virtual Assistant")

    elif "hello alexa" in data_btn or "hye alexa" in data_btn or "hay alexa" in data_btn: 
        return speak_and_return("Hey sir, how can I help you!") 

    elif "how are you" in data_btn:
        return speak_and_return("I am doing great these days, sir")   

    elif "thanku" in data_btn or "thanks" in data_btn:
        return speak_and_return("It's my pleasure sir to stay with you")     

    elif "good morning" in data_btn:
        return speak_and_return("Good morning sir, I think you might need some help")   

    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        return speak_and_return(Time)

    elif "shutdown" in data_btn or "quit" in data_btn:
        return speak_and_return("Ok sir")

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        return speak_and_return("Gaana.com is now ready for you, enjoy your music")

    elif 'open google' in data_btn or 'google' in data_btn:
        webbrowser.get().open('https://google.com/')
        return speak_and_return("Google is now opening for you")

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        webbrowser.get().open('https://youtube.com/')
        return speak_and_return("YouTube is open")

    elif 'open music' in data_btn: 
        os.startfile(r"C:\\Users\\KUSHAGRA G\\Downloads\\whip-afro-dancehall-music-110235.mp3")
        return speak_and_return("Song is playing...")

    else:
        response = chat_local(data_btn)
        return speak_and_return(response)
