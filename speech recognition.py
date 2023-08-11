import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound

def get_audio():
        recorder = sr.Recognizer()
        with sr.Microphone() as source:
            print("say something.....")
            audio = recorder.listen(source, 20, 10)

        print('Recognizing text...')
        text = recorder.recognize_google(audio)
        print(f"You said:{text}")
        return text

def speech(text):
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")
    
    if "youtube" in text.lower():
        print("okay, i will bring that up on youtube for you.")
        pywhatkit.playonyt(text)
    elif "joke" in text.lower():
        print("konck konck, who is there? Boo. Boo who? Do not cry, i was just telling a joke")
    else:
        pywhatkit.search(text)

if __name__ == '__main__':
    text = get_audio()
    speech(text)