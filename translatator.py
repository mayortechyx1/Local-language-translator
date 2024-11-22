import speech_recognition as sr
from deep_translator import GoogleTranslator

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"you said {text}")

    igbo    = GoogleTranslator(source='auto', target="").translate(text)
    hausa   = GoogleTranslator(source='auto', target="").translate(text)
    yoruba  = GoogleTranslator(source='auto', target="").translate(text)

    print(igbo)
    print(hausa)
    print(yoruba)

except:
    print("come again?")
