from output.voice_output import speak
import webbrowser

def play_spotify():
    speak("Opening Spotify...")
    webbrowser.open("https://open.spotify.com/")
