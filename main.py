import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import captureImg as ci   #pip install captureImg
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hacktober\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to hacktober' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hacktoberyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend hacktober bhai. I am not able to send this email")    
        elif 'capture image' in query:
            ci.captureImg()
            
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
	def digital_assistant(data):
#     global listening
   elif "how are you" in data:
        listening = True
        respond("I am well")

    elif "what time is it" in data:
        listening = True
        respond(ctime())

    elif "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on Dante, I will show you where " + data[2] + " is.")
        maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
        os.system(maps_arg)
        
    elif "what is the weather in" in data:
        listening = True
        api_key = "Your_API_key"
        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
        data = data.split(" ")
        location = str(data[5])
        url = weather_url + "appid=" + api_key + "&q=" + location 
        js = requests.get(url).json() 
        elif js["cod"] != "404": 
            weather = js["main"] 
            temp = weather["temp"] 
            hum = weather["humidity"] 
            desc = js["weather"][0]["description"]
            resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
            respond(resp_string)
        else: 
            respond("City Not Found") 
    elif "stop listening" in data:
        listening = False
        print('Listening stopped')
    return listening
			
time.sleep(3)
