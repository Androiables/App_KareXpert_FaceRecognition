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
            print(img)
            print(detector.matchFace(img))
    else:
        print(detector.matchFace(path))

# trainModel()
path = input("Enter the Image Path: ")

detect(path)