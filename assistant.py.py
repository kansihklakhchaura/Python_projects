import openai
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

# Function to handle the commands
def handle_command(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif 'open google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    elif 'open code' in query:
        code_path = "path_to_your_code_editor"
        os.startfile(code_path)
    else:
        if query != "None":
            response = model.generate_content(query +"in 30 words")
            speak(response.text)

#gemini integration
import google.generativeai as genai
apikey="AIzaSyBNcCSJgiRYPXLG_rqotzHrGC0EUu5CnXY"
genai.configure(api_key=apikey)
model = genai.GenerativeModel('gemini-1.5-flash')




# Main function to run the assistant
if __name__ == "__main__":
    speak("Initializing assistant")
    while True:
        command = take_command()
        handle_command(command)


         