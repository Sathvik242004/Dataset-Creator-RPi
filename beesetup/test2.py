import RPi.GPIO as GPIO
import time
import cv2
import os
from datetime import datetime

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
button_pin = 22
buzzer_pin = 27

# Set up the button pin as input with internal pull-up resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)


# Initialize previous button state
prev_button_state = GPIO.LOW

def capture_images(folder):
    # Initialize the webcams
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f")
    print(timestamp)
    capLeft = cv2.VideoCapture(2)
    capRight = cv2.VideoCapture(0)
    
    if not (capLeft.isOpened() and capRight.isOpened()):
        print("Error: Couldn't access the cameras")
        return

    # Capture frame-by-frame
    ret1, frameL = capLeft.read()
    cv2.imwrite(os.path.join(folder, f'{timestamp}_img_L.jpg'), frameL)
    ret2, frameR = capRight.read()
    cv2.imwrite(os.path.join(folder, f'{timestamp}_img_R.jpg'), frameR)    

    capLeft.release()
    capRight.release()
    cv2.destroyAllWindows()
    print("Images saved successfully you can remove the frame...")
    GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn buzzer ON



try:
    folder = "captured_images"
    if not os.path.exists(folder):
        os.makedirs(folder)
    while True:
        # Read button state
        button_state = GPIO.input(button_pin)

        # Check if button state changed from low to high
        if button_state == GPIO.HIGH and prev_button_state == GPIO.LOW:
            print("Frame detected")
            capture_images(folder)

        # Check if button state changed from high to low
        if button_state == GPIO.LOW and prev_button_state == GPIO.HIGH:
            print("Frame removed")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn buzzer ON


        # Update previous button state
        prev_button_state = button_state

        # Wait a short delay to avoid multiple detections due to bouncing
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
