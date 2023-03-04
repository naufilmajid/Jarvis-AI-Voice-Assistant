import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening hogye jani!")    
    speak("I am jarvis Bhai. Please tell me how may I help you")    


def takecommand():
    #it takes microphone input from the user and returns string output.
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("He's Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing......")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)

        print("say that again please......")
        return "NONE"
    return query

def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()




if __name__ == "__main__":
    #speak("Naufil is a good boy")
    wishMe()
    while True:
        query=takecommand().lower()

    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.......')
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strtime}")

        elif 'open code' in query:
            codePath="D:\\vscode\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'exit' in query:
            speak("Thanks for giving me your time Naufil")
            exit()

        #FOR MUSIC    
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'email to naufil' in query:
            try:
                speak("what should I say?")
                content=takecommand()
                to="naufilmajid@gmail.com"
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry jani nhi gye email. kuch masla hai")




