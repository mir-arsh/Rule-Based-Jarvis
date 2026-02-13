import speech_recognition as sr
import webbrowser
import pyttsx3
import channelLibrary

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif c.lower().endswith("youtube"):
        channel = c.lower().split(" ")[1]
        link = channelLibrary.channels[channel]
        webbrowser.open(link)
    elif "google" in c.lower():
        search = c.lower().replace("google", "").strip()
        search1 = search.replace("search", "").strip()
        search2 = search1.replace("on", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search2}")
    else:
        print("Sorry! I did not understand that command.")
        print("You can add that in my code logic.")


if __name__ == "__main__":
    speak("Initializing...")
    while True:
        # Listen for user's wake word
        # Obtain audio from microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            order = r.recognize_google(audio)
            if(order.lower() == "ai"):
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("AI active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Sorry! I did not get that.")