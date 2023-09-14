from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog,QMessageBox,QPushButton
import cv2
import face_recognition
import numpy as np
import os
import utils
from custom_dialog import CustomDialog

class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        loadUi("./outputwindow.ui", self)   #Load output form UI

        self.image = None
        self.recogBtn: QPushButton = self.RecognizeButton
        self.rcdBtn: QPushButton = self.RecordButton
        self.encode_list = []

    @pyqtSlot()
    def startVideo(self, camera_name):
        """
        :param camera_name: Link to webcam or usb camera
        :return:
        """
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
        else:
            self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)  # create Timer
        path = 'Images'     #The path to read the face recognition image
        if not os.path.exists(path):
            os.mkdir(path)
        # List of face codes and face names under the path
        images = []
        self.people_names = []
        self.encode_list = []
        self.TimeList1 = []
        self.TimeList2 = []
        people_list = os.listdir(path)

        for cl in people_list:
            cur_img = cv2.imread(f'{path}/{cl}')
            images.append(cur_img)
            self.people_names.append(os.path.splitext(cl)[0])

        # for img in images:
        #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #     boxes = face_recognition.face_locations(img)
        #     encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
        #     self.encode_list.append(encodes_cur_frame)
        self.timer.timeout.connect(self.update_frame)  # Timeout connection output
        self.timer.start(10)

    def face_rec_(self, frame):
        """
        :param frame: camera capture
        :param encode_list_known: Entered face code
        :param people_names: Entered face name
        :return:
        """
        # Face recognition part
        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
        name = "unknown"    #Unknown face recognition as unknown
        status = utils.FACE_NO_DETECTED

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(self.encode_list, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(self.encode_list, encodeFace)
            best_match_index = np.argmin(face_dis)
            if faceLoc is not None:
                status = utils.FACE_DETECTED

            if match[best_match_index]:
                name = self.people_names[best_match_index].upper()
        self.StatusLabel.setText(status)
        if utils.is_face_detected(status):
            self.NameLabel.setText(name)
        else:
            self.NameLabel.setText("")

        return frame
    
    def record_face(self, frame):
        # Face recognition part
        encodes_cur_frame = face_recognition.face_encodings(frame, face_recognition.face_locations(frame))[0]
        self.encode_list.append(encodes_cur_frame)
        print(self.encode_list)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success")
        else:
            print("Failed")

    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("hint")
        msg.setInformativeText("message append")
        msg.setWindowTitle("notification")
        msg.setDetailedText("The content is as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def update_frame(self):
        _, self.image = self.capture.read()
        self.displayImage(self.image, window=1)

    def displayImage(self, image, window=1):
        """
        :param image: Image captured from camera
        :param encode_list: Recognized face recognition code
        :param people_names: Name of person whose face has been recognized
        :param window: form
        :return:
        """
        image = cv2.resize(image, (640, 480))   #Define recognition area size
        try:
            if self.recogBtn.isChecked():
                self.recogBtn.setEnabled(False)
                image = self.face_rec_(image)
                self.recogBtn.setChecked(False)
                self.recogBtn.setEnabled(True)
            elif self.rcdBtn.isChecked():
                self.rcdBtn.setEnabled(False)
                self.record_face(image)
                self.rcdBtn.setEnabled(True)
                self.rcdBtn.setChecked(False)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)
