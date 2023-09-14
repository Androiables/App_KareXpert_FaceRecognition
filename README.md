# Face Recognition Application

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

The Face Recognition Application is a Python-based desktop application developed using PyQt5, OpenCV (cv2), and the face_recognition library. This application enables real-time face recognition through a webcam or USB camera, allowing you to identify individuals based on pre-defined images.

## Features

- **Real-time Face Recognition:** Utilize your webcam or USB camera to perform real-time face recognition.
- **Recognize Known Faces:** Recognizes faces based on pre-defined images stored in the "Images" directory.
- **Display Recognized Faces:** Displays recognized faces with their corresponding names in real-time.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- PyQt5
- OpenCV (cv2)
- face_recognition
- NumPy

You can install these dependencies using the following command:

```bash
pip install PyQt5 opencv-python-headless face_recognition numpy
```
or
```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/face-recognition-app.git

2. Navigate to the project directory:
    ```bash
    cd face-recognition-app
    ```

## Usage

1. Run the application using the following command:
    ```bash
    python main.py
    ```


2. When the application starts, you will see a graphical user interface (GUI) with the following options:

- **Camera Source:** Choose either "Webcam" or provide the path to your USB camera (e.g., "/dev/video0").
- **Start:** Click this button to begin the face recognition process.

3. The application will start capturing frames from the selected camera source and perform face recognition.

4. Recognized faces will be displayed in real-time with their corresponding names (if found in the pre-defined images).

## Configuration

To add faces for recognition, follow these steps:

1. Place images of individuals you want to recognize in the "Images" directory.

- Each image should be named after the person it represents (e.g., "john.jpg").
- Ensure that the images are in JPG format.

2. Adjust recognition parameters in the code, such as the tolerance level, to fine-tune the recognition accuracy based on your requirements.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them.

5. Push your changes to your forked repository.

6. Create a pull request on the original repository, describing your changes.

## Acknowledgments

- The [face_recognition library](https://github.com/ageitgey/face_recognition) for its contribution to face recognition technology.

We appreciate your interest and welcome any suggestions or contributions to improve this project.
