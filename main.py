import speech_recognition as sr
import pyttsx3
import webbrowser
import difflib
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

def get_best_song_match(command_text):
    matches = difflib.get_close_matches(command_text, musiclibrary.music.keys(), n=1, cutoff=0.4)
    return matches[0] if matches else None

if __name__ == "__main__":
    speak("Initializing Alexa. Say 'Alexa' to wake me up.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print("Heard:", command)

            if "alexa" in command:
                speak("Yes,gourab  how can I help?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print("Command:", command)

                # Open Google
                if "google" in command:
                    speak("Opening Google")
                    webbrowser.open("https://www.google.com")

                # Open YouTube
                elif "youtube" in command:
                    speak("Opening YouTube")
                    webbrowser.open("https://www.youtube.com")

                # Play music
                elif "play" in command:
                    song_request = command.split("play", 1)[1].strip()
                    matched_song = get_best_song_match(song_request)

                    if matched_song:
                        speak(f"Playing {matched_song}")
                        webbrowser.open(musiclibrary.music[matched_song])
                    else:
                        speak(f"Sorry, I couldn't find '{song_request}' in your music library.")

                else:
                    speak("Sorry, I don't know that command yet.")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Recognizer error: {e}")




