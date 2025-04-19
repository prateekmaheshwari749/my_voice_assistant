import speech_recognition as sr
import webbrowser
import pyttsx3
import mss
import requests
import cv2
import os
import musiclibrary
import pyaudio

# Initialize speech recognition and text-to-speech
recogniser = sr.Recognizer()
engine = pyttsx3.init()

# News API Key (Ensure it's valid)
NEWS_API_KEY = "d099f9dfdacb4f41949f075ca6fd9743"

# Sample Music Library (Replace with actual music URLs)
music_library=musiclibrary.music
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """Process voice commands."""
    command = command.lower()
    
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "weather" in command:
        speak("Opening weather map")
        webbrowser.open("https://windy.com")
    
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    
    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
    
    elif "snapchat" in command:
        speak("Opening Snapchat")
        webbrowser.open("https://snapchat.com")
    
    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    

    
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        if song in music_library:
            speak(f"Playing {song}")
            webbrowser.open(music_library[song])
        else:
            speak("Sorry, I couldn't find that song.")
    
    elif "news" in command:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for article in data["articles"][:5]:
                speak(f"Title: {article['title']}")
        else:
            speak("Sorry, I couldn't fetch the news.")
    
    elif "pic" in command:
        speak("Capturing an image")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            speak("Image captured successfully")
        cap.release()
        cv2.destroyAllWindows()
    
    elif "screenshot" in command:
        with mss.mss() as sct:
            sct.shot(output="screenshot.png")
            speak("Screenshot taken")

    


def listen_for_commands():
    """Listen for the wake word 'Jarvis' and process commands."""
    recogniser = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recogniser.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recogniser.recognize_google(audio).lower()
                
                if wake_word == "jarvis":
                    speak("Yes, how can I help you?")
                    with sr.Microphone() as source:
                        audio = recogniser.listen(source)
                        command = recogniser.recognize_google(audio)
                        process_command(command)
                
                elif wake_word in ["stop", "exit", "quit", "shutdown"]:
                    speak("Goodbye!")
                    break
                
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results, check your internet connection")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    speak("Hi, I am your voice assistant. Say 'Jarvis' to wake me up.")
    listen_for_commands()

    
