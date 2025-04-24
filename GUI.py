from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import speak 
import os



root = Tk()
root.title("AI Assistant")
root.geometry("1024x750")
root.resizable(False, False)

themes = [
    {
        "name": "VSCode Dark",
        "bg": "#1e1e1e", "fg": "#d4d4d4",
        "text_bg": "#252526", "entry_bg": "#3c3c3c", "button_bg": "#0e639c"
    },
    {
        "name": "GitHub Dark",
        "bg": "#0d1117", "fg": "#c9d1d9",
        "text_bg": "#161b22", "entry_bg": "#21262d", "button_bg": "#238636"
    },
    {
        "name": "Nord",
        "bg": "#2e3440", "fg": "#d8dee9",
        "text_bg": "#3b4252", "entry_bg": "#434c5e", "button_bg": "#81a1c1"
    },
    {
        "name": "Charcoal",
        "bg": "#2a2a2a", "fg": "#e0e0e0",
        "text_bg": "#333333", "entry_bg": "#4a4a4a", "button_bg": "#606060"
    },
    {
        "name": "Cyber Night",
        "bg": "#1f1b24", "fg": "#f8f8f8",
        "text_bg": "#292433", "entry_bg": "#3a3445", "button_bg": "#ff4081"
    },
    {
        "name": "Monokai Dark",
        "bg": "#272822", "fg": "#f8f8f2",
        "text_bg": "#3e3d32", "entry_bg": "#49483e", "button_bg": "#f92672"
    }
]

current_theme_index = 0
current_theme = themes[current_theme_index]

def apply_theme():
    root.config(bg=current_theme["bg"])
    frame.config(bg=current_theme["bg"])
    text_label.config(bg=current_theme["bg"], fg=current_theme["fg"])
    text.config(bg=current_theme["text_bg"], fg=current_theme["fg"])
    entry.config(bg=current_theme["entry_bg"], fg=current_theme["fg"])
    for btn in [Button1, Button2, Button3, theme_button, stop_button]:
        btn.config(bg=current_theme["button_bg"], fg=current_theme["fg"])

def toggle_theme():
    global current_theme_index, current_theme
    current_theme_index = (current_theme_index + 1) % len(themes)
    current_theme = themes[current_theme_index]
    apply_theme()
    theme_button.config(text=f"🎨 Theme: {current_theme['name']}")

def on_closing():
    speak.stop_speaking()  # Stop any ongoing speech
    root.destroy()         # Close GUI
    os._exit(0)

def ask():
    user_val = speech_to_text.speech_to_text()
    if not user_val:
        text.insert(END, '👤 You: (Could not understand audio)\n')
        return

    text.insert(END, f'👤 You: {user_val}\n')
    text.see(END)

    def update_bot_text(full_response):
        text.insert(END, f'🤖 Bot: {full_response}\n')
        text.see(END)

    response = action.Action(user_val)
    speak.speak(response, update_callback=update_bot_text)
    if response.lower() == "ok sir":
        root.destroy()

def send():
    user_input = entry.get()
    entry.delete(0, END)

    text.insert(END, f'👤 You: {user_input}\n')
    text.see(END)

    def update_bot_text(full_response):
        text.insert(END, f'🤖 Bot: {full_response}\n\n')
        text.see(END)

    response = action.Action(user_input)
    speak.speak(response, update_callback=update_bot_text)
    if response.lower() == "ok sir":
        root.destroy()

def delete_text():
    text.delete('1.0', END)

def stop_speech():
    speak.stop_speaking()

# GUI layout
frame = Frame(root, padx=20, pady=10, relief=RAISED, bd=2)
frame.place(x=50, y=20, width=920, height=220)

text_label = Label(frame, text="AI Voice Assistant", font=("Helvetica", 18, "bold"))
text_label.pack(pady=10)

try:
    image = Image.open("C:\\Users\\KUSHAGRA G\\Desktop\\Python projects\\Virtual Asistant\\assistant.png")
    image = image.resize((100, 100))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(frame, image=photo)
    image_label.pack(pady=10)
except FileNotFoundError:
    image_label = Label(frame, text="Image not found", font=("Helvetica", 10))
    image_label.pack(pady=10)

scrollbar = Scrollbar(root)
scrollbar.place(x=965, y=260, height=300)

text = Text(root, font=("Courier New", 12), yscrollcommand=scrollbar.set, wrap=WORD)
text.place(x=50, y=260, width=915, height=300)
scrollbar.config(command=text.yview)
text.tag_config("bot_start", foreground="lightgreen")

entry = Entry(root, font=("Helvetica", 12), justify=CENTER)
entry.place(x=100, y=580, width=800, height=40)

btn_style = {'font': ("Helvetica", 12, "bold"), 'relief': SOLID, 'bd': 2}
Button1 = Button(root, text="🎤 ASK", command=ask, **btn_style)
Button1.place(x=150, y=640, width=100, height=40)

Button2 = Button(root, text="📝 Send", command=send, **btn_style)
Button2.place(x=270, y=640, width=100, height=40)

Button3 = Button(root, text="❌ Clear", command=delete_text, **btn_style)
Button3.place(x=390, y=640, width=100, height=40)

stop_button = Button(root, text="⏹ Stop", command=stop_speech, **btn_style)
stop_button.place(x=510, y=640, width=100, height=40)

theme_button = Button(root, text="🌓 Toggle Theme", command=toggle_theme, **btn_style)
theme_button.place(x=630, y=640, width=180, height=40)

apply_theme()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
