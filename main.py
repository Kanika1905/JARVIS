import speech_recognition as sr
import webbrowser
import pyttsx3
import video

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)   # engine text bolega jo function k argument me hoga
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        learn=c.lower().split(" ")[1]
        link=video.videos[learn]
        webbrowser.open(link)

if __name__=="__main__":
    speak("initializing jarvis")
    while True:

        r=sr.Recognizer()
        print("recognizing")
    
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)

            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes, How may I help you")
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)


           
        except Exception as e:
            print("could not understand audio")

