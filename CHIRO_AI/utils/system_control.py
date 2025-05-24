import os
from output.voice_output import speak

def open_app(app_name):
    try:
        if "chrome" in app_name:
            os.system("start chrome")
        elif "notepad" in app_name:
            os.system("start notepad")
        elif "calculator" in app_name:
            os.system("start calc")
        else:
            speak(f"Sorry, I can't open {app_name} yet.")
            return
        speak(f"Opening {app_name}")
    except Exception as e:
        speak("An error occurred while trying to open the application.")
