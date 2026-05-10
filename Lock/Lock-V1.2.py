import ctypes
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.media_play_pause:
        print("Locking your computer: This should work on Windows normally")
        try:
            
            ctypes.windll.user32.LockWorkStation()
        except Exception as e:
            print(f"Error locking: {e}")

print("Press the media_play_pause key on your bluetooth device. If it doesn't work, view KgKeys for more help.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
