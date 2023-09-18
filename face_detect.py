import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
import pickle
import time
import utils

class FaceDetector:
    def __init__(self, TrainingImagePath: str):
        self.encode_list = []
        self.ResultMap={}
        self.trainingSet = None
        self.classifier = None
        self.testDatagen = ImageDataGenerator()
        batch_size = len(utils.getList(TrainingImagePath)) * 2
        self.trainDatagen = ImageDataGenerator(
                    shear_range=0.1,
                    zoom_range=0.1,
                    horizontal_flip=True)
        self.trainingSet = self.trainDatagen.flow_from_directory(
                                TrainingImagePath,
                                target_size=(64, 64),
                                batch_size=batch_size,
                                class_mode='categorical')
            
        self.testSet = self.testDatagen.flow_from_directory(
                                TrainingImagePath,
                                target_size=(64, 64),
                                batch_size=batch_size,
                                class_mode='categorical')

        self.neurons = None

    def createClassifier(self):
 
        self.classifier = Sequential()
        ''' STEP--1 Convolution
        # Adding the first layer of CNN
        # we are using the format (64,64,3) because we are using TensorFlow backend
        # It means 3 matrix of size (64X64) pixels representing Red, Green and Blue components of pixels
        '''
        self.classifier.add(Convolution2D(32, kernel_size=(5, 5), strides=(1, 1), input_shape=(64,64,3), activation='relu'))
        
        '''# STEP--2 MAX Pooling'''
        self.classifier.add(MaxPool2D(pool_size=(2,2)))
        
        '''############## ADDITIONAL LAYER of CONVOLUTION for better accuracy #################'''
        self.classifier.add(Convolution2D(64, kernel_size=(5, 5), strides=(1, 1), activation='relu'))
        
        self.classifier.add(MaxPool2D(pool_size=(2,2)))
        
        '''# STEP--3 FLattening'''
        self.classifier.add(Flatten())
        
        '''# STEP--4 Fully Connected Neural Network'''
        self.classifier.add(Dense(64, activation='relu'))
        
        self.classifier.add(Dense(self.neurons, activation='softmax'))
        
        '''# Compiling the CNN'''
        #self.classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.classifier.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=["accuracy"])

    def trainModel(self):
        TrainClasses=self.trainingSet.class_indices

        for faceValue,faceName in zip(TrainClasses.values(),TrainClasses.keys()):
            self.ResultMap[faceValue]=faceName

        # Saving the face map for future reference
        with open("ResultsMap.pkl", 'wb') as fileWriteStream:
            pickle.dump(self.ResultMap, fileWriteStream)

        # The model will give answer as a numeric tag
        # This mapping will help to get the corresponding face name for it
        print("Mapping of Face and its ID",self.ResultMap)

        # The number of neurons for the output layer is equal to the number of faces
        self.neurons=len(self.ResultMap)

        self.createClassifier()

        # Measuring the time taken by the model to train
        StartTime=time.time()
        
        # Starting the model training
        self.classifier.fit_generator(
                            self.trainingSet,
                            steps_per_epoch=4,
                            epochs=10,
                            validation_data=self.testSet,
                            validation_steps=30)
        
        EndTime=time.time()
        print("###### Total Time Taken: ", round((EndTime-StartTime)/60), 'Minutes ######')


    def matchFace(self, imgPath: str):
        test_image=image.load_img(imgPath,target_size=(64, 64))
        test_image=image.img_to_array(test_image)
        
        test_image=np.expand_dims(test_image,axis=0)
        
        result=self.classifier.predict(test_image,verbose=0)
        
        print('####'*10)
        print('Prediction is: ',self.ResultMap[np.argmax(result)])
