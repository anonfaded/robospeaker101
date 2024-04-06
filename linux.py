from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    # Load the saved audio file
    audio = AudioSegment.from_mp3("output.mp3")

    # Play the audio
    play(audio)

    # Remove the temporary audio file
    os.remove("output.mp3")

if __name__ == "__main__":
    text = input("Enter the text to speak: ")
    speak(text)
