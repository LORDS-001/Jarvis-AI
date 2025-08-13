import os
import datetime
import webbrowser as wb
import smtplib
import speech_recognition as sr
import wikipedia
import pyttsx3
import pyautogui as pag
import psutil as ps
import pyjokes as pj

def speak(audio):
    engine  = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"Today's date is {day} {month} {year}")

def time_and_date():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    Date = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"The current time is {Time}")
    speak(f"The current date is {Date}")

def Hour():
    Hour = datetime.datetime.now().hour
    if Hour >= 6 and Hour <12:
        speak("Good Morning, LORDS!")
    elif Hour >=12 and Hour <18:
        speak("Good Afternoon LORDS!")
    elif Hour >=18 and Hour <24:
        speak("Good Evening LORDS!")
    else:
        speak("Good Night LORDS!")

def greetings():
    speak("Welcome Back LORDS!")
    Hour()
    speak("How can I help you Supreme Ruler of the Universe")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry, I did not understand that. Please repeat.")
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adedokundaniel16@gmail.com', 'alphalords')
    server.sendmail('adedokundaniel16@gmail.com', to, content)
    server.close()

def screenshot():
    img = pag.screenshot()
    img.save("C:\\Users\\adedo\\Jarvis-AI\\ss.png")

def cpubattery():
    usage = str(ps.cpu_percent())
    speak("CPU is at " + usage + "percent")
    battery = ps.sensors_battery()
    speak("Battery is at")
    speak(str(battery.percent) + "percent")

def jokes():
    speak(pj.get_joke())

if __name__ == "__main__":
    greetings()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching ...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adedokundaniel16@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print(e)
                speak("LORDS, I am not able to send this email.")

        elif 'search' in query:
            speak("What should I search ?")
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif 'play songs' in query:
            songs_dir = "C:\\Users\\adedo\\Music"
            songs = os.listdir(songs_dir)
            speak("What song should I play")
            search = takeCommand().lower()
            matches = [song for song in songs if search in song.lower()]
            if matches:
                speak(f"Playing {matches[0]}")
                os.startfile(os.path.join(songs_dir, matches[0]))
            else:
                speak("Sorry, I could not find that song.")

        elif 'remember' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open ('data.txt', 'w', encoding='utf-8')
            remember.write(data)
            remember.close

        elif 'do you know anything' in query:
            remeber = open('data.txt', 'r', encoding='utf-8')
            speak("You told me to remember that " + remeber.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done! I have taken a screenshot.")

        elif 'cpu' in query:
            cpubattery()
            speak("CPU and battery status checked.")

        elif 'joke' in query:
            jokes()
            speak("I hope you enjoyed the joke.")

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t l")

        elif 'restart' in query:
            os.system("shutdown /r /t l")

        elif 'offline' in query:
            Hour()
            speak("Going offline, LORDS!")
            quit()