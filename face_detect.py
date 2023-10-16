import cv2
import face_recognition
import pickle as pk
import numpy as np
import utils
import os

class FaceDetector:
    def __init__(self):
        self.encode_list: dict = {'names': [], 'data': []}


    def trainModel(self, TrainingImagePath: str):
        # Load Saved Data the encode_list
        try:
            with open("encode_list.pkl", 'rb') as fileReadStream:
                self.encode_list = pk.load(fileReadStream)
        except:
            print("Empty Files Creating a new")

        peopleList = utils.getList(TrainingImagePath)

        for img in peopleList:
            name = os.path.splitext(img)[0].split('/')[-1]
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            self.encode_list['data'].append(encodes_cur_frame)
            self.encode_list['names'].append(name)

        # Save the encode_list data to a file using pickle
        with open("encode_list.pkl", 'wb') as fileWriteStream:
            pk.dump(self.encode_list, fileWriteStream)

    def __loadModel(self):
        # Load the encode_list data from the saved file
        with open("encode_list.pkl", 'rb') as fileReaderStream:
            self.encode_list = pk.load(fileReaderStream)

    def matchFace(self, imgPath: str):
        self.__loadModel()
        img = cv2.imread(imgPath)
        curr = face_recognition.face_locations(img)
        encodes_cur_frame = face_recognition.face_encodings(img,curr)

        for encodeFace in encodes_cur_frame:
            match = face_recognition.compare_faces(self.encode_list['data'], encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(self.encode_list['data'], encodeFace)
            best_match_index = np.argmin(face_dis)

            if match[best_match_index]:
                return self.encode_list['names'][best_match_index]
        return False
    
    def faceExists(self, imgPath: str):
        img = cv2.imread(imgPath)
        curr: list = face_recognition.face_locations(img)
        return len(curr) > 0