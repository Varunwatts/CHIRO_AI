from input.speech_input import listen
from output.voice_output import speak
from core.face_auth import is_user_present
from core.task_executor import execute_task
from gui.interface import setup_gui
import threading

def run_assistant():
    while True:
        print("Listening for command...")
        command = listen()
        if command:
            print(f"You said: {command}")
            speak(f"You said: {command}")
            execute_task(command)

def main():
    print("CHIRO: Scanning for authorized face...")
    speak("Scanning for authorized face")

    if is_user_present():
        print("CHIRO: Access Granted. Starting interface...")
        speak("Access Granted. Hello, I am CHIRO.")

        # Start assistant listening in a background thread
        assistant_thread = threading.Thread(target=run_assistant, daemon=True)
        assistant_thread.start()

        # Start GUI on the main thread
        setup_gui()
    else:
        print("CHIRO: Access Denied.")
        speak("Access Denied. Face not recognized.")

if __name__ == "__main__":
    main()
