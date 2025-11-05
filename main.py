import time
import speech_recognition as sr 
import  webbrowser
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()
#-----------------------------
# changing voice in this 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is usually female voice
# ---------------------------

def speak(Text):
    engine.say(Text)
    engine.runAndWait()
#processing the given command ..= >
def processCommand(command):
    print(command)
    if "open google" in command.lower():
       speak("opening google ...")
       time.sleep(2)
       webbrowser.open("https://www.chrome.com")

    elif  "open facebook" in command.lower():
       engine.say("opening face Book ...")
       time.sleep(2)
       webbrowser.open("https://www.facebook.com")
    elif "open youtube" in command.lower():
        speak("opening youtube ...")
        time.sleep(2)
        webbrowser.open("https://www.youtube.com")
    elif "play" in command.lower():
        song_name = command.lower().replace("play ","").strip()
        if song_name in music_library.music:
            link = music_library.music[song_name]
            speak(f"playing {song_name}")
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    else:
        print("this project on con.")

if __name__ == "__main__":
    speak("Initializing Nexa...... ")
    while True:
        # listen for the wake word "jarvis"
        # obtion audio form the microphone
        r = sr.Recognizer()
        print("recognizing.... ")
        try:
            with sr.Microphone() as source :
                print("listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word  = r.recognize_google(audio)
            if(word.lower() =="nexa" ):
                engine.say("yes .... ")
                 # listen for command .. 
                with sr.Microphone() as source :
                    print("Nexa active ...")
                    audio = r.listen(source)  
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("sphinx could not understand audio ")
        except Exception as e:
            print(f"sphinx error : {e}")