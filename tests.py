from face_detect import FaceDetector
import utils

def getAccurancy():
    detector = FaceDetector()
    trainingImg = input("Enter the training Sample: ")
    detector.trainModel(trainingImg)

    imagesPath = input("Enter the Images Path: ")

    print(detector.matchFace(imagesPath))

getAccurancy()