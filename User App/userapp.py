import os
import glob
import cv2
from cv2 import VideoCapture, imwrite
import dlib
import csv
import sys
from itertools import chain 
import pygame, time
from pygame.locals import *
import numpy as np
import tensorflow as tf 

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

model = tf.keras.Sequential([
    tf.keras.layers.Dense(50, input_shape=(136,)), # input_shape?
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.load_weights('shittyModel.h5')

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera

print('Welcome to the DeepPomodoro user app!')

while True:
    #take photo
    s, img = cam.read()
    if s: imwrite("photo.jpg",img) #save image

    #run face detector
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_in_image = detector(img_gray, 0)

    landmarks_list = np.array([[]])

    for face in faces_in_image:
        print("face detected")
        # assign the facial landmarks
        landmarks = predictor(img_gray, face)
        
        # unpack the 68 landmark coordinates from the dlib object into a list 
        for i in range(0, landmarks.num_parts):
            landmarks_list = np.append(landmarks_list, [[landmarks.part(i).x]], axis = 1)
            landmarks_list = np.append(landmarks_list, [[landmarks.part(i).y]], axis = 1)

    print(landmarks_list)
    output = model.predict(landmarks_list)

    print('Focus level: ' + str(output))

    # Write landmarks to csv
    #with open("landmarks.csv", 'a') as myfile:
    #   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #    wr.writerow(landmarks_flattened)
