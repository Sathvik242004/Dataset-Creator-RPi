import cv2
def list_video_devices():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        else:
            _, _ = cap.read()  # Read a frame just to ensure the camera is opened
            print(f"Video device {index}: {cap.get(cv2.CAP_PROP_BACKEND)}")
            cap.release()
            index += 1


def capture_photo(file_name):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Couldn't access the webcam")
        return

    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Failed to capture frame")
        return

    # Save the captured frame as an image
    cv2.imwrite(file_name, frame)

    # Release the webcam
    cap.release()

    print(f"Photo captured and saved as '{file_name}'")

if __name__ == "__main__":
    file_name = "captured_photo.jpg"  # Change the file name and extension as needed
    list_video_devices()


    
