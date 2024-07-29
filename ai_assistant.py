import speech_recognition as sr
import webbrowser
import smtplib
import pyttsx3
import datetime
import wikipedia
import os
import cv2
import random
import pyjokes


engine = pyttsx3.init()


r = sr.Recognizer()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good morning!")
    elif hour >= 12 and hour < 18:
        engine.say("Good afternoon!")
    else:
        engine.say("Good evening!")
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query


def execute_command(query):
    
    if 'greet' in query:
        greet()

    elif 'open' in query.lower() and 'youtube' in query.lower():
        webbrowser.open("https://www.youtube.com")

 
    elif 'email' in query.lower():
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            message = input("Enter the message: ")
            server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", message)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(e)

 
    elif 'search' in query.lower():
        query = query.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")


    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        engine.say(f"The time is {strTime}")
        engine.runAndWait()


    elif 'date' in query.lower():
        strDate = datetime.datetime.now().strftime("%Y-%m-%d")
        engine.say(f"Today's date is {strDate}")
        engine.runAndWait()


    elif 'wikipedia' in query.lower():
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        engine.say(results)
        engine.runAndWait()

 

    elif 'joke' in query.lower():
        engine.say(pyjokes.get_joke())
        engine.runAndWait()


    elif 'play' in query.lower():
        songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
        engine.say("Playing a random song")
        engine.runAndWait()
        os.startfile(random.choice(songs))




    else:
        engine.say("I don't understand")
        engine.runAndWait()

if __name__ == '__main__':
    while True:
        query = take_command().lower()
        if query == "exit":
            break
        execute_command(query)
