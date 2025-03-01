import musiclibrary
import speech_recognition as sr 
import webbrowser
import pyttsx3
import mss

import requests
import cv2
from openai import OpenAI
import os
from flask import Flask , render_template




recogniser=sr.Recognizer()

engine = pyttsx3.init()

newsapi="d099f9dfdacb4f41949f075ca6fd9743"







def speak(text):
    engine.say(text) 
    engine.runAndWait()



# def recognize_face():
#     video_capture = cv2.VideoCapture(0)

#     known_image = face_recognition.load_image_file("known_person.jpg")
#     known_encoding = face_recognition.face_encodings(known_image)[0]

#     while True:
#         ret, frame = video_capture.read()
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces([known_encoding], face_encoding)
#             if matches[0]:
#                 speak("Welcome back, sir!")
#                 return  # Stop function once face is recognized

#     video_capture.release()
#     cv2.destroyAllWindows()








def processcomand(c):
    
    
    if "google" in c.lower():
        #for opening google 
        speak("opening google")
        webbrowser.open("https://google.com")

    elif "weather" in c.lower():
        speak("opening weather map")
        webbrowser.open("https://windy.com")

    
    
    elif "facebook" in c.lower():
         #for opening facebook
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    
    
    
    elif "youtube" in c.lower():
         #for opening youtube
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
        
    
    
    elif "instagram" in c.lower():
         #for opening instagram
        speak("opening instagram")
        webbrowser.open("https://instagram.com")

    
    
    elif "snapchat" in c.lower():
         #for opening snapchat
        speak("opening snapchat")
        webbrowser.open("https://snapchat.com")

   
   
    elif "linkedin" in c.lower():
         #for opening linkdein
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    
    
    
    elif c.lower().startswith("play"):
         #for playing a music
        speak("playing music")
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)

    
    
    elif "news" in c.lower():
        api_key = "d099f9dfdacb4f41949f075ca6fd9743"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=d099f9dfdacb4f41949f075ca6fd9743"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for article in data["articles"][:5]:  # Print the first 5 headlines
                speak(f"Title: {article['title']}")


    
    
    elif "pic" in c.lower():
        
        app = Flask(__name__)

        IMAGE_PATH = "static/captured_image.jpg"

        def capture_image():
            cap = cv2.VideoCapture(0)  # Open webcam
            ret, frame = cap.read()
            
            if ret:
                cv2.imwrite(IMAGE_PATH, frame)  # Save the image
                print(f"Image saved at {IMAGE_PATH}")
            
            cap.release()
            cv2.destroyAllWindows()

        @app.route("/")
        def index():
            return render_template("index.html", image_path=IMAGE_PATH)

        @app.route("/capture")
        def capture():
            capture_image()  # Take a photo when user visits "/capture"
            return render_template("index.html", image_path=IMAGE_PATH)

        if __name__ == "__main__":
            app.run(debug=True)

            webbrowser.open(IMAGE_PATH)

    

    elif "screenshot" in c.lower():
        with mss.mss() as sct:
            sct.shot(output="screenshot.png") 


    

        

    
        
    





if __name__=="__main__":
    speak("Hii, i am your voice Assistant")


while True:
    r = sr.Recognizer()
    #listen wait for bro 

    # recognize speech using Sphinx
    print("Wait a second...")
    
    
    try:
        
        with sr.Microphone() as source:
            print("Please say something")
            speak("Hey , I'am listening ...")
            
            audio = r.listen(source,timeout=3,phrase_time_limit=3)
        
            word= r.recognize_google(audio)
        
       
       
        if word.lower()=="jarvis" :
            
            speak("Yes")
            #for listening                        
            
            with sr.Microphone() as source:
                print("Ask your question")
                speak("Hey , how can i help you")
            
                audio = r.listen(source)
            
                com= r.recognize_google(audio)

                processcomand(com)

        
        
        elif word.lower()=="stop":
            break
        
    
    
    
    except Exception as e:
            print("Error; {0}".format(e))
    