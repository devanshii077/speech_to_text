import customtkinter as ctk
from tkinter import filedialog
import speech_recognition as sr
from datetime import datetime

# === Setup Appearance === #
ctk.set_appearance_mode("System")  # System / Light / Dark
ctk.set_default_color_theme("green")

# === App Window === #
app = ctk.CTk()
app.title("🎙️ Speech-to-Text App")
app.geometry("720x600")
app.resizable(False, False)

# === Functions === #
def transcribe_microphone():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            animate_status("🎤 Listening... Please speak", "orange")
            app.update()
            audio = recognizer.listen(source, timeout=6)
            text = recognizer.recognize_google(audio)
            display_text(text)
            save_text(text)
            animate_status("✅ Transcription complete & saved!", "lightgreen")
    except sr.UnknownValueError:
        animate_status("❌ Couldn't understand audio", "red")
    except sr.RequestError:
        animate_status("❌ Network/API Error", "red")
    except Exception as e:
        animate_status(f"⚠️ Error: {str(e)}", "red")

def transcribe_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV Audio", "*.wav")])
    if not file_path:
        return
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            display_text(text)
            save_text(text)
            animate_status("✅ File transcribed & saved!", "lightgreen")
    except Exception as e:
        animate_status(f"⚠️ Error: {str(e)}", "red")

def display_text(text):
    textbox.delete("0.0", "end")
    textbox.insert("0.0", text)

def save_text(text):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transcription_{now}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def clear_text():
    textbox.delete("0.0", "end")
    animate_status("🧹 Text cleared", "skyblue")

def animate_status(message, color):
    status.configure(text=message, text_color=color)
    status.after(3000, lambda: status.configure(text=""))

def toggle_mode():
    selected = mode_switch.get()
    ctk.set_appearance_mode("Dark" if selected == "Dark" else "Light")
    animate_status(f"🌓 Mode: {selected}", "yellow")

# === UI Layout === #

# Title
title = ctk.CTkLabel(app, text="✨ Speech-to-Text Transcriber ✨", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=20)

# Mode switch
mode_switch = ctk.CTkOptionMenu(app, values=["Light", "Dark"], command=lambda _: toggle_mode())
mode_switch.set("System")
mode_switch.pack(pady=10)

# Buttons
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=10)

mic_btn = ctk.CTkButton(btn_frame, text="🎙️ Record from Mic", command=transcribe_microphone, width=180, height=45, corner_radius=25, font=("Arial", 14))
mic_btn.grid(row=0, column=0, padx=10, pady=10)

file_btn = ctk.CTkButton(btn_frame, text="📂 Upload WAV File", command=transcribe_file, width=180, height=45, corner_radius=25, font=("Arial", 14))
file_btn.grid(row=0, column=1, padx=10, pady=10)

clear_btn = ctk.CTkButton(app, text="🧼 Clear Text", command=clear_text, width=140, corner_radius=20)
clear_btn.pack(pady=5)

# Textbox for displaying transcript
textbox = ctk.CTkTextbox(app, width=650, height=260, font=("Consolas", 14), border_width=2, corner_radius=15)
textbox.pack(pady=15)

# Status bar
status = ctk.CTkLabel(app, text="", font=("Arial", 14, "italic"))
status.pack(pady=5)

# Footer
footer = ctk.CTkLabel(app, text="🛠️ Made by Devanshi | Powered by Python", font=("Arial", 12))
footer.pack(side="bottom", pady=10)

# Run
app.mainloop()
