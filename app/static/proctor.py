import cv2
import os
import time
import threading
import pyaudio
import numpy as np
from scipy.io import wavfile

# Define paths to Haar cascades
models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../models"))
face_cascade_path = os.path.join(models_dir, 'haarcascade_frontalface_default.xml')
eye_cascade_path = os.path.join(models_dir, 'haarcascade_eye.xml')

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Verify Haar cascade loading
if face_cascade.empty() or eye_cascade.empty():
    print("Error: Unable to load Haar cascade files. Check the file paths.")
    exit()

# Function to monitor the camera
def monitor_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to access the camera.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('Proctoring Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to monitor audio
def monitor_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    last_log_time = 0
    log_interval = 1  # Log once every second
    noise_threshold = 0.1  # Adjust threshold for noise sensitivity

    while True:
        data = stream.read(1024, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16)
        volume = np.sqrt(np.mean(audio_data**2)) / 32768  # Normalize volume

        if volume > noise_threshold:
            current_time = time.time()
            if current_time - last_log_time > log_interval:
                print("Speech or noise detected!")
                last_log_time = current_time

# Run both monitors in separate threads
if __name__ == "__main__":
    camera_thread = threading.Thread(target=monitor_camera, daemon=True)
    audio_thread = threading.Thread(target=monitor_audio, daemon=True)

    camera_thread.start()
    audio_thread.start()

    camera_thread.join()
    audio_thread.join()
