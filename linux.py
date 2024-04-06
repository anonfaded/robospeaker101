from gtts import gTTS
from playsound import playsound

def speak(text, speed=1.0, lang='en'):
    # Adjust the speed of speech using the speed parameter
    tts = gTTS(text=text, lang=lang, slow=False if speed >= 1.0 else True)
    tts.save("temp.mp3")  # Save the speech to a temporary file
    playsound("temp.mp3")  # Play the speech using playsound

# Example usage:
speak("HThe gTTS library doesn't provide direct control over speech rate or voice gender. However, you can achieve similar effects by adjusting the speed of the generated speech using the speed parameter and selecting different languages to get different voices.", speed=1.0)  # Faster speech