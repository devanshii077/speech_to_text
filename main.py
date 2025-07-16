# Updated for GitHub push

import speech_recognition as sr

recognizer = sr.Recognizer()

print("Choose input method:")
print("1. Microphone")
print("2. WAV file")
choice = input("Enter 1 or 2: ")

if choice == "1":
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
elif choice == "2":
    filename = input("Enter the WAV file name (with extension): ")
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
else:
    print("❌ Invalid choice")
    exit()

try:
    text = recognizer.recognize_google(audio)
    print("\n📝 Transcription:\n", text)

    # 💾 Save to a text file
    with open("transcription_output.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("\n✅ Transcription saved to 'transcription_output.txt'")

except sr.UnknownValueError:
    print("❌ Could not understand the audio.")
except sr.RequestError:
    print("❌ Could not request results from Google Speech Recognition.")
