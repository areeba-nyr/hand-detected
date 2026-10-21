# Hand Detection with Python

A real-time hand detection project built with Python, OpenCV, and MediaPipe. It uses your webcam to detect your hand, track hand landmarks, and highlight the position of your index fingertip.

## Features

- Real-time webcam video
- Hand detection using MediaPipe
- Hand landmark visualization
- Index fingertip tracking with a green dot
- Live fingertip coordinates
- Keyboard controls to exit the program

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

## Requirements

- Python 3.12 recommended
- A working webcam
- Windows, macOS, or Linux with compatible Python packages

## Installation

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd hand-detection
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment**

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Run the project**

```bash
python hand_detection.py
```

## Controls

- `Q` — Close the program
- `Esc` — Exit the camera window

## How It Works

1. OpenCV accesses the webcam and captures video frames.
2. The frames are mirrored and converted to RGB.
3. MediaPipe detects the hand and identifies its landmarks.
4. The program highlights the index fingertip and displays its coordinates.
5. If no hand is detected, the window displays a message asking you to show your hand.

## Project Structure

```text
hand-detection/
├── hand_detection.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/  (local only; not uploaded)
```

## Future Improvements

- Detect multiple hands
- Add gesture recognition
- Recognize hand signs
- Build interactive computer vision projects

## Acknowledgements

Built using the open-source [MediaPipe](https://github.com/google-ai-edge/mediapipe) and [OpenCV](https://github.com/opencv/opencv) libraries.

---

Created as a hands-on Python computer vision project.
