from output.voice_output import speak
import requests

def report_weather():
    # Replace with your API key
    API_KEY = "2d3782a64afcc059decc048ce8b9486a"
    CITY = "Chirala"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        condition = response["weather"][0]["description"]
        speak(f"Today's weather in {CITY} is {condition} with a temperature of {temp} degrees Celsius.")
    except:
        speak("Sorry, I couldn't fetch the weather.")
