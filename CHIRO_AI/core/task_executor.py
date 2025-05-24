# core/task_executor.py

from output.voice_output import speak
from utils.open_youtube import play_youtube_video
from utils.weather import report_weather
from utils.spotify import play_spotify
from utils.system_control import open_app

def execute_task(command):
    command = command.lower()

    if "youtube" in command or "play" in command:
        play_youtube_video(command)

    elif "weather" in command:
        report_weather()

    elif "spotify" in command:
        play_spotify()

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_app(app_name)

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")
