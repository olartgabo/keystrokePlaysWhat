import os
import keyboard
import platform
import time
import pygame


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_FILE = os.path.join(BASE_DIR, "ANIMALS.mp3")

def set_volume_max():
    system = platform.system()
    if system == "Windows":
        os.system("nircmd setsysvolume 65535") 
    elif system == "Linux":
        os.system("pactl set-sink-volume @DEFAULT_SINK@ 100%")
    elif system == "Darwin": 
        os.system("osascript -e 'set volume output volume 100'")

def play_media():
    pygame.mixer.init()
    pygame.mixer.music.load(MEDIA_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def main():
    print("CARGANDO ULTI DE WARWICK")
    while True:
        if keyboard.is_pressed("r"):
            set_volume_max()
            play_media()
            time.sleep(1) 

if __name__ == "__main__":
    main()
