# ProTraq - Exam Proctoring Tool

## Overview
ProTraq is an AI-based exam proctoring tool designed to monitor exam-takers' behavior during online quizzes. It ensures exam integrity by detecting whether the examinee:
- Looks away from the screen
- Speaks during the exam
- Produces any background noise
- Switches to another screen

This project integrates image processing using OpenCV for face and eye detection and audio monitoring to detect noise or speech. It also includes a quiz system for assessing users.

## Features
- **Eye Tracking**: Detects if the user looks away from the screen using a webcam.
- **Speech Detection**: Uses a microphone to listen for any sounds or speech during the exam.
- **Screen Switching Detection**: Flags an error if the user switches away from the exam screen.
- **Sample Quiz**: Displays a sample quiz with multiple-choice questions and calculates the user's score upon submission.
- **Real-Time Monitoring**: Runs continuously during the quiz, monitoring the user's actions.

## Requirements

- Python 3.x
- OpenCV
- pyaudio
- Flask
- HTML, CSS, JS (for the frontend quiz and user interaction)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/protraq.git
cd protraq
```

### 2. Install dependencies
Create and activate a virtual environment, then install the required packages:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
```

Make sure to include the required libraries like:
- `opencv-python`
- `pyaudio`
- `Flask`
- `numpy`
- `pillow`

### 3. Download Haar Cascades
Download the following Haar Cascade XML files and place them in the `models/` directory:
- [Haar Cascade for Face Detection](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- [Haar Cascade for Eye Detection](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

### 4. Run the Application
To start the Flask server, run:

```bash
python app.py
```

This will launch the app, and you can access the exam proctoring tool in your browser at:

```
http://127.0.0.1:5000
```

### 5. Frontend Quiz Setup
The frontend quiz is built using HTML, CSS, and JavaScript. The questions and options are fetched from the Flask backend. The user can submit the quiz, and the score will be returned based on the answers selected.

### 6. Running the Proctoring Tool
When you start the quiz, the proctoring tool will:
- Activate the webcam to detect face and eye movement.
- Start the microphone to detect any speech or background noise.
- Monitor if the user switches from the quiz window.

If any suspicious activity is detected, the tool will issue a warning.

## File Structure
```
protraq/
├── app.py                    # Main Flask app
├── requirements.txt          # Python dependencies
├── models/                   # Contains Haar cascade XML files
│   ├── haarcascade_frontalface_default.xml
│   └── haarcascade_eye.xml
├── static/                   # Frontend files (HTML, CSS, JS)
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md                 # Project documentation
```

## Troubleshooting

1. **Error loading Haar cascade files**: Ensure the paths to the cascade files (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) are correct and the files are in the `models/` directory.
   
2. **Speech Detection Issues**: Ensure your microphone is connected and accessible. You may need to install additional dependencies for `pyaudio` based on your OS.

3. **Webcam Access**: Ensure your browser or Python script has permission to access the webcam.

4. **Quiz Not Working**: Verify the Flask routes for quiz handling (`/get_quiz`, `/submit_quiz`) are correctly defined and returning the right data.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
- OpenCV for face and eye detection.
- pyaudio for speech and noise detection.
