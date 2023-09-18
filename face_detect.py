import face_recognition
import numpy as np
import cv2
import utils

class FaceDetector:
    def __init__(self):
        self.encode_list = []


    def trainModel(self, TrainingImagePath: str):
        peopleList = utils.getList(TrainingImagePath)
        print(peopleList)

        for img in peopleList:
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            self.encode_list.append(encodes_cur_frame)


    def matchFace(self, imgPath: str):
        img = cv2.imread(imgPath)
        curr = face_recognition.face_locations(img)
        encodes_cur_frame = face_recognition.face_encodings(img,curr)

        for encodeFace in encodes_cur_frame:
            match = face_recognition.compare_faces(self.encode_list, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(self.encode_list, encodeFace)
            best_match_index = np.argmin(face_dis)

            if match[best_match_index]:
                return True
        return False