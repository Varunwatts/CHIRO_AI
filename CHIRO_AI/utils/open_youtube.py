# utils/open_youtube.py

import pywhatkit
import pyttsx3

def play_youtube_video(command):
    """
    Extracts the video name from the command and plays it on YouTube.
    Example: "play Starboy by The Weeknd"
    """
    try:
        # Strip the command prefix
        if "play" in command:
            video = command.lower().replace("play", "").strip()
            response = f"Playing {video} on YouTube..."
            print(f"CHIRO: {response}")
            
            # Voice feedback
            engine = pyttsx3.init()
            engine.say(response)
            engine.runAndWait()
            
            # Play the video
            pywhatkit.playonyt(video)
        else:
            print("CHIRO: Could not understand the YouTube request.")
    except Exception as e:
        print(f"CHIRO: Failed to play YouTube video due to: {e}")
