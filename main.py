import pygame
import time
import speech_recognition as sr 
import  webbrowser
import pyttsx3
import music_library
from openai import OpenAI
from datetime import datetime
from gtts import gTTS
import os
import cv2
import  datetime
import requests
import json
import AI_NEXA
import pyautogui as p
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
#-----------------------------                                          
# changing voice in this 
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  # 1 is usually female voice
# ---------------------------
def Aiprocess(command):
    client = OpenAI(
    
    api_key=AI_NEXA.api_key
)
    response = client.chat.completions.create(
    model="gpt-4o-mini",  # Fast & smart model
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant  , whose name Nexa and date of birth  24 januery 2025  made by Hardik. ,give short ans , nexa is an girl ai  assistant} "},
        {"role": "user", "content": command}
    ]
)
    return(response.choices[0].message.content)
#--------------------------------------------------------------------
# face detector fun. 
# def faceDetector():
#     print("Cascade exists:", os.path.exists("cow_cascade.xml"))

# video_capture = cv2.VideoCapture(0)
# cow_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# while True:
#     ret, video_data = video_capture.read()
#     if not ret:
#         break
#     gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

#      face  = cow_cap.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30)
#     )

#     for (x, y, w, h) in cows:
#         cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     cv2.imshow("HARDIK", video_data)
#     if cv2.waitKey(10) & 0xFF == ord('a'):
#         break
# video_capture.release()
# cv2.destroyAllWindows()
def speak(Text):
    tts = gTTS(Text)
    tts.save('text.mp3')

# Initialize pygame mixer
    pygame.mixer.init()

    # Load your audio file

    pygame.mixer.music.load("text.mp3")  # Replace with your file path

    # Play the audio
    pygame.mixer.music.play()

    # print("Playing music... Press Enter to stop.")
    # input()  # Keeps the program running until you press Enter
    # Stop the music
    while pygame.mixer.music.get_busy():
      time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    os.remove("text.mp3")


#processing the given command ..= >
def processCommand(command):
    print(command)
    if "open google" in command.lower():
       speak("opening google ...")
       time.sleep(1)
       p.press('win')
       time.sleep(1)
       p.write('google',interval=0.3)
       p.press('enter')
    elif "open chrome" in command.lower():
       speak("opening chroe ...")
       time.sleep(1)
       p.press('win')
       time.sleep(1)
       p.write('chrome',interval=0.3)
       p.press('enter')
    elif  "open facebook" in command.lower():
       speak("opening face Book ...")
       time.sleep(2)
       webbrowser.open("https://www.facebook.com")
    elif"vs code" in command.lower():
        speak("Opening  visual studio code  ")
        time.sleep(1)
        p.press('win')
        time.sleep(1)
        p.write('vs code',interval=0.3)
        p.press('enter')
    elif "open youtube" in command.lower():
        speak("opening youtube ...")
        time.sleep(1)
        p.press('win')
        time.sleep(1)
        p.write('You tube',interval=0.3)
        p.press('enter')
        speak("Sir, kya aap chahte hain ki main kuch content search karu?")
        with sr.Microphone() as source :
                print("listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                ans = r.recognize_google(audio)
        if ans.lower() == ['yes','ha','haan'] or 'yes' in  ans.lower() or 'ha' in ans.lower():
            speak("Bataiye, main kya search karu?")
            with sr.Microphone() as source :
                print("listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                content = r.recognize_google(audio)
            p.press('/')
            p.write(f"{content}",interval=0.4)
            p.press("enter")
            speak("Enjoy kijiye, sir!")
        else:
            speak("Theek hai, agar kuch aur kaam ho to bol dijiye, main yahan hoon.")
    elif "play" in command.lower():
        song_name = command.lower().replace("play ","").strip()
        if song_name in music_library.music:
            link = music_library.music[song_name]
            speak(f"playing {song_name}")
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    elif "stop" in command.lower() or "exit" in command.lower() or "quit" in command.lower():
        speak("Goodbye sir, Nexa shutting down...")
        pygame.mixer.music.stop()
        exit()
    elif "chatbot" in command.lower():
        
        API_KEY = AI_NEXA.api_key
        client = OpenAI(api_key=API_KEY)

        while True:
            user_input = input("🧑 You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 Chat ended. Goodbye!")
                break
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant created by Hardik."},
                    {"role": "user", "content": user_input}
                ]
            )

            print("\n🤖 AI:", response.choices[0].message.content, "\n")

    elif "notepad" in command.lower():
        os.system("notepad")
    elif "face detector" in command.lower():
        # faceDetector()
        speak("sory my owner don't allow to open camera ")
    elif "time" in command.lower():
            now = datetime.datetime.now()
            speak(f"Current Date and Time: {now}")
    # elif "weather" in command.lower() or "moosum" in command.lower():
        # while True:
    elif "weather" in command.lower() or "mausam" in command.lower():
            with sr.Microphone() as source:
                speak("Sir, aapki city ka naam bataiye.")
                audio = r.listen(source)
                city = r.recognize_google(audio)

            api = AI_NEXA.weatherApi
            url = f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=no"
            response = requests.get(url)
            weather_dec = json.loads(response.text)

            day = "afternoon" if weather_dec["current"]["is_day"] == 1 else "night"

            speak(f"Temperature in {city} is {weather_dec['current']['temp_c']} degree celsius.")
            speak("Sir, kya aap aur weather details chahte ho?")

            with sr.Microphone() as source:
                audio = r.listen(source)
                user_ans = r.recognize_google(audio)

            if "yes" in user_ans.lower() or "ha" in user_ans.lower():
                if day == "afternoon":
                    speak(
                        f"It is afternoon. Last update at {weather_dec['current']['last_updated']}. "
                        f"In {city}, temperature is {weather_dec['current']['temp_f']} Fahrenheit "
                        f"and {weather_dec['current']['temp_c']} Celsius."
                    )
                else:
                    speak(
                        f"It is night. Last update at {weather_dec['current']['last_updated']}. "
                        f"In {city}, temperature is {weather_dec['current']['temp_f']} Fahrenheit."
                    )

    #    import datetime
    # Get the current local date and time
    # Get the current date only
    # today = datetime.date.today()
    # speak(f"Current Date: {today}")
    else:
        ans =  Aiprocess(command)
        with open("AI_ans.txt","a") as f:
            f.write("\n")
            f.write(ans)
        speak(ans)


if __name__ == "__main__":
    speak("Powering up systems. ")
    # speak("Voice recognition loaded.")
    # speak("Welcome back, Hardik. All systems are green.")
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
                speak("yes sir ........."
                ". ")
                     # listen for command ..
                while True: 
                    with sr.Microphone() as source :
                        print("Nexa active ...")
                        audio = r.listen(source)  
                        command = r.recognize_google(audio)
                        processCommand(command)

        except sr.UnknownValueError:
            print("sphinx could not understand audio ")
        except Exception as e:
            print(f"sphinx error : {e}")