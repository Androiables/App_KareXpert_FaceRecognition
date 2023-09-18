from face_detect import FaceDetector
import utils

# FaceDetector
detector = FaceDetector()

def trainModel():
    trainingImg = input("Enter the training Sample: ")
    detector.trainModel(trainingImg)

def detect(path: str):
    if utils.isDir(path):
        for img in utils.getList(path):
            detector.matchFace(img)
    else:
        detector.matchFace(path)


trainModel()
path = input("Enter the Image Path: ")

detect(path)