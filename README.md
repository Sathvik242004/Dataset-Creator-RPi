---

## Project Description

This project consists of three functional Python scripts:

1. **`beesetup/capture.py`**: This script utilizes the webcam to capture photos. It takes a photo when a button is pressed.

2. **`backup/usb_detector.py`**: This script monitors USB devices connected to the Raspberry Pi using the Pyudev module. When a USB device is detected, it automatically mounts the USB drive and copies all files from the `captured_images` folder to the drive.

3. **`lastexe/finalising.py`**: This script provides the status of the Raspberry Pi. Additionally, it handles operations such as clearing the `captured_images` folder and shutting down the Pi.

### GPIOs
- **OVERALL_LED_PIN**: 11 (Indicates the status of the Pi)
- **BUTTON_PIN**: 13 (Used to delete the images in `captured_images` and shutdown the Pi)
- **status**: 2 (Indicates USB status)
- **button_pin**: 22 (Used to capture images)
- **buzzer_pin**: 27 (Indicates the status of the captured images)

### Instructions
To use this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Sathvik242004/Dataset-creator-rpi.git
   ```
2. Navigate to the project directory:
   ```
   cd bee
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Execute the launcher script:
   ```
   sh launcher.sh
   ```

---

This README provides an overview of the project, including its components, GPIO pin configurations, and instructions for getting started. Feel free to reach out if you have any questions or need further assistance.
Contact: kunurusathvik4@gmail.com
Happy coding!
