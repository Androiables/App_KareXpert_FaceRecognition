from face_detect import FaceDetector
import utils
from timeit import default_timer as timer

def getAccurancy():
    trainingImg = input("Enter the training Sample: ")
    imagesPath = input("Enter the Images Path: ")

    detector = FaceDetector(trainingImg)
    detector.trainModel()
    print(detector.matchFace(imagesPath))

getAccurancy()