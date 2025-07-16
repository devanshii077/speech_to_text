from pydub import AudioSegment
from pydub.utils import which
import os

# ✅ Your actual FFmpeg bin folder path
ffmpeg_path = r"C:\Users\Devanshi\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

# 🧠 Set FFmpeg and FFprobe paths manually
os.environ["PATH"] += os.pathsep + ffmpeg_path
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

def convert_mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    print(f"✅ Converted {mp3_path} to {wav_path}")

# 🧪 Run the conversion
convert_mp3_to_wav("sample.mp3", "sample.wav")
