from pynput import keyboard

def on_press(key):
    # Exact name! BTW ctrl & other keys show up as text, not a ctrl or smth
    print(f"Key detected: {key}")

print("You can press keys. If you are debugging, try not to spam keys or it'll be hard to find the one you want")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
