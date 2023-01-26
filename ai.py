import pyttsx3
import datetime
import speech_recognition as ms
import wikipedia

engine=pyttsx3.init()
voices=engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishpeeps():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello Sir! I am an AI Assistant called as Christopher!Please tell me if you need something and if I can help you in that")

def takeorder():
    y=ms.Recognizer()
    with ms.Microphone() as source:
        print("Enculcating....")
        y.pause_threshold=1
        audio=y.listen(source)
    try:
        print("Recognizing....")
        query=y.recognize_google(audio,language='en-in')
        print("user has ordered: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__=="__main__":
    wishpeeps()
    while True:
        query=takeorder().lower()

        if wikipedia in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
