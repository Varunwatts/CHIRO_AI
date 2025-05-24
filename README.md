# CHIRO_AI
# 🤖 CHIRO AI Assistant

CHIRO is a personal AI assistant inspired by J.A.R.V.I.S. and Baymax. It uses facial recognition for secure activation and voice commands to perform a wide range of smart tasks like playing YouTube videos, reporting weather, playing songs on Spotify, and opening system applications.

## 🧠 Features

- 🎙️ Voice-controlled interface
- 🧑‍💻 Facial authentication using webcam
- 📺 Play any YouTube video by voice
- 🌦️ Get current weather updates
- 🎧 Spotify music playback via voice
- 🖥️ Open system apps with natural commands
- 🧸 GUI interface with Baymax-style image

## 📁 Project Structure

CHIRO_AI/
├── assets/
│ └── baymax.png
├── core/
│ ├── face_auth.py
│ ├── speech_input.py
│ ├── task_executor.py
├── gui/
│ └── interface.py
├── output/
│ └── voice_output.py
├── utils/
│ ├── open_youtube.py
│ ├── open_weather.py
│ ├── open_spotify.py
│ └── system_control.py
├── main.py

## Install Required Modules
pip install -r requirements.txt
pip install face_recognition opencv-python pyttsx3 speechrecognition pytube3 python-vlc requests
Note: You must also install dlib (used by face_recognition). On Windows, it’s easiest with:
pip install dlib

## Get Your Weather API Key
Sign up at: https://openweathermap.org/
Generate a free API key.
Replace "YOUR_OPENWEATHERMAP_API_KEY" in utils/open_weather.py with your actual key.
API_KEY = "YOUR_API_KEY"

## Add Baymax Image
Place a baymax.png image inside the assets/ folder to power the GUI interface.

## 🎤 How to Use
Run the assistant:
python main.py
Look into your webcam for facial authentication.

## Speak a command, e.g.:
> “Play Time Less by The Weeknd”
> “What's the weather today?”
> “Open Spotify”
> Say “exit” or “stop” to terminate.

## 🛠️ Commands Supported
Command Example	Function
"Play [song/video] on YouTube"	YouTube playback
"Play [song] on Spotify"	Spotify control
"What's the weather like today?"	Weather update
"Open [app name]"	Open system applications
"Exit" or "Stop"	Quit the assistant
