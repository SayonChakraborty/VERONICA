import pyttsx3
import pyaudio
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pyjokes
from twilio.rest import Client
import requests
import time
import winshell
import json
from googlesearch import *
import subprocess
import win32com.client as winclpip
import ctypes
import json
from urllib.request import urlopen 

import cv2





















engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, Veronica online !')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'google' in query:
            speak('Opening Google')
            webbrowser.open('www.google.co.in')

        elif 'gmail' in query:
            speak('opening gmail')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
            

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("myboolbool2404@gmail.com", 'sayon2404')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'no' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query: 
         
            speak("Your favourite playsit is on your screen sir ")
            webbrowser.open("https://music.youtube.com/playlist?list=PLRBp0Fe2Gpgn8Y9qI-p0aTxVtw8onBSFj")
    
           
       
        elif 'whatsapp' in query: 
         
            speak("opening whatsapp\n")
            webbrowser.open("https://web.whatsapp.com/")
           

     
           

        elif 'the time' in query: 
            strTime = datetime.datetime.now()                                                                                                                         
            speak(f"Sir, the time is {strTime}") 
            
            
        elif "who i am" in query: 
            speak("You are talking to me then definately you are a human.") 
            
        elif "jokes" in query:
            print(pyjokes.get_joke()) 
            speak(pyjokes.get_joke())   
            
            
        elif "calculate" in query:
            app_id = "J9K5ER-22PAY78L75"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak(answer)
        elif "what's your name" in query or "What is your name" in query: 

        # timepass Commands

            speak("My friends call me VERONICA") 
            print("My friends call me VERONICA")    
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by SAYON as a Minor project")  
        elif "do u harm me" in query or "are u bad" in query:  
            speak("I am a just a freindly helpful Assistant")
        elif "thought on ai" in query or " your views on artificial intelligence" in query:  
            speak("Artificial Intelligence makes human better") 
        elif "siri" in query or "google assistant" in query or "cortona" in query or "alexa" in query:
            speak("I have no resistance to helpful assistance")    
        elif "how are you" in query or "what is up" in query:  
            speak("I am Fine Sir")    
        elif "what your name mean" in query: 
            speak("My name is quite weird but it stands for - Very Easy Rodent Oriented Netwide Index to Computerized Archives")  
        elif "how are you" in query or "what is up" in query:  
            speak("I am Fine Sir") 
        elif "love" in query:
            speak("It's a 7th sense that destroy all 6 senses")  
        elif "how humans are" in query or " what you think about humans" in query:  
            speak("Humans are really intelligent thnakful to them to bring me here")      
        elif "marry me" in query or "married" in query:  
            speak("I am married to my work sir")   
        elif "how are you" in query or "what is up" in query:  
            speak("I am Fine Sir") 
        elif "can you be my girlfreind" in query:
            speak("Such a hard question give me sometime to think")    
        elif "I am fine too" in query or "I am good" in query:  
            speak("Glad to know that you are fine Sir")  
         
       

            # Programs To Run System Commands 
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "veronica Camera ", "img.jpg")  
            speak ("photo save in your gallery")  
        elif 'powerpoint ' in query or 'presentation' in query:
            speak("opening Power Point presentation") 
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)    
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       'D:\wallpapers', 
                                                       0) 
            speak("Background changed succesfully") 
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation()     
        
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")   
            
        elif "show what you write down " in query: 
            speak("Showing Notes") 
            file = open("veronica.txt", "r")  
            print(file.read()) 
            speak(file.read(6))     

        

               
        elif "hibernate" in query or "sleep" in query: 

            speak("Hibernating") 
            subprocess.call("shutdown / h") 
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 


         
        

        elif "translate" in query:
            webbrowser.open("https://translate.google.co.in/" )
            speak("Opening Translator") 
        elif "can you be my girlfreind" in query:
            speak("Such a hard question give me sometime to think")
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Veronica Camera ", "img.jpg")  
            speak("Done sir") 
        elif "word" in query:
            word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(word)
            speak("opening word")   
        elif "music player" in query:
            music= r"%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe"
            os.startfile(music)
            speak("opening music")       
        elif "valorant" in query:
            valorant = r"C:\Riot Games\Riot Client\RiotClientServices.exe" 
            os.startfile(valorant)
            speak("opening valorant")
        elif "steam" in query:
            steam = r"C:\Program Files (x86)\Steam\Steam.exe"
            os.startfile(steam)
            speak("opening steam") 
        elif "chrome" in query:
            chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome)
            speak("opening chrome")     

        elif "set a reminder"in query:
            speak("What shall I remind you about?")
            query = str(input())
            speak("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
        elif "what can you do" in query or "how are you helpful" in query:
            speak("I can help you to search anything open applications and doing calculations and lot of stuffs ")   
        elif "weather" in query: 
            speak ("city name")
            query = myCommand()
            webbrowser.open("google weather "+  query)
        elif "where is" in query: 
            chrome_path = r'C:\Program Files (x86)\Google\Chrome'
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("google maps" + location + "") 
        elif 'time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}")    
            
        elif "hotstar" in query:
            webbrowser.open("https://www.hotstar.com/in/?utm_source=onebox&utm_campaign=IPL2020&utm_term=live")
            speak ("opening Hotstar")
        elif "amazon prime"   in query:
            webbrowser.open("https://www.primevideo.com/region/eu/ref=av_auth_return_redir")
            speak ("opening amazon prime")
        elif "Shopping" in query:
            webbrowser.open("https://www.amazon.in/?ie=UTF8&ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_Cj0KCQjw1PSDBhDbARIsAPeTqrcpyDQFF3LpOzx038fj9RpybgEScTetGcibpoSGERWuyWhG8_UiK7saAucREALw_wcB_k_&ext_vrnc=hi&gclid=Cj0KCQjw1PSDBhDbARIsAPeTqrcpyDQFF3LpOzx038fj9RpybgEScTetGcibpoSGERWuyWhG8_UiK7saAucREALw_wcB")
            speak ("opening Shopping Site")
                
              
           


 
            

            

            
            



                





          
       




            





              

         


                                    
     
            

        else:


            chrome_path = r'C:\Program Files (x86)\Google\Chrome'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
                speak ("Looking for"  + query ) 
        speak('Anything Else  Sir!')
        
        