import pyttsx3
from pathlib import Path

def genvoice(instance) -> tuple():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[2].id)
    engine.save_to_file(instance.eng, f'{instance.eng}.mp3')
    engine.runAndWait()
    
    return Path.cwd(), f'{instance.eng}.mp3'
