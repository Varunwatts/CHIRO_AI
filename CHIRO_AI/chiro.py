import cv2
import face_recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import webbrowser

# ========== SPEECH FUNCTIONS ==========

engine = pyttsx3.init()

def speak(text):
    print(f"CHIRO: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is unavailable.")
        return ""

# ========== FACE RECOGNITION ==========

def is_user_present():
    known_image = face_recognition.load_image_file("my_face.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    video_capture = cv2.VideoCapture(0)
    recognized = False

    for _ in range(10):
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]  # BGR to RGB

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding in face_encodings:
            matches = face_recognition.compare_faces([known_encoding], encoding)
            if True in matches:
                recognized = True
                break
        if recognized:
            break

    video_capture.release()
    return recognized

# ========== ACTION HANDLER ==========

def perform_action(command):
    if "play music" in command:
        music_dir = "C:\Users\venka\Music"  # Replace this with your music folder path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music.")
        else:
            speak("No music files found.")

    elif "play" in command and "youtube" in command:
        video = command.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {video} on YouTube")
        pywhatkit.playonyt(video)

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't understand that command yet.")
    return True

# ========== MAIN FUNCTION ==========

if __name__ == "__main__":
    speak("Scanning for authorized face...")
    if is_user_present():
        speak("Welcome back, I'm CHIRO. What can I do for you?")
        while True:
            user_command = listen()
            if not perform_action(user_command):
                break
    else:
        speak("Unauthorized user. Access denied.")
