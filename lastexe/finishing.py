from gpiozero import Button, LED
from signal import pause
import subprocess
import time
# Define the GPIO pin number where your button is connected

BUTTON_PIN = 13
OVERALL_LED_PIN = 11

# Initialize the Button object with a debounce time of 0.5 seconds
button = Button(BUTTON_PIN, bounce_time=0.5)

# Initialize the LED object
overall_led = LED(OVERALL_LED_PIN)

# Flag to keep track of button state
button_pressed = False

# Function to be called when the button is pressed
def button_pressed_action():
    global button_pressed
    if not button_pressed:
        print("Initializing deletion...")
        subprocess.run(['sudo', 'rm', '-fr', '/home/bee/captured_images'])  # Fixed path
        print("Deletion successful...")
        time.sleep(5)
        subprocess.run(['sudo','shutdown','-h','now'])
        button_pressed = True
        # Blink the LED once when the button is pressed
        overall_led.blink(on_time=0.5, off_time=0.5, n=1)

# Function to be called when the button is released
def button_released_action():
    global button_pressed
    if button_pressed:
        print("Button is released")
        button_pressed = False

# Assign the event handlers
button.when_pressed = button_pressed_action
button.when_released = button_released_action

# Turn on the overall LED initially
overall_led.on()

# Keep the script running to continue monitoring button events
pause()