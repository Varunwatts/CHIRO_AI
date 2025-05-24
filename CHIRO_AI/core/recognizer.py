def recognize_command(text):
    text = text.lower()
    if "time" in text:
        return "time"
    elif "youtube" in text:
        return "youtube"
    elif "music" in text:
        return "music"
    elif "exit" in text:
        return "exit"
    return "unknown"
