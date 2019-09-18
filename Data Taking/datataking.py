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

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)

alert = 1
mood = 1

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera

print('Welcome to the DeepPomodoro data taking script!')
print("Current alertness (a to switch): " + str(alert))
print("Current mood (m to switch):      " + str(mood))
print('Press m to change mood, or a to change alertness.\n')

while True:
    #take photo
    s, img = cam.read()
    if s: imwrite("photo.jpg",img) #save image

    #read and delete photo
    list_of_files = glob.glob('*') 
    latest_file = max(list_of_files, key=os.path.getctime)
    img = cv2.imread(latest_file, 1)
    os.remove(latest_file)

    #run face detector
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_in_image = detector(img_gray, 0)
    landmarks_list = []

    for face in faces_in_image:
        # assign the facial landmarks
        landmarks = predictor(img_gray, face)
        
        # unpack the 68 landmark coordinates from the dlib object into a list 
        for i in range(0, landmarks.num_parts):
            landmarks_list.append((landmarks.part(i).x, landmarks.part(i).y))

    landmarks_list.append((mood, alert))
    landmarks_flattened = list(chain.from_iterable(landmarks_list)) 

    # Write landmarks to csv
    with open("landmarks.csv", 'a') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(landmarks_flattened)

    for event in pygame.event.get():
        if (event.type == KEYUP):
            if(event.key == pygame.K_m):
                if (mood == 1):
                    print("you have indicated MOOD = 0")
                    mood = 0
                else:
                    print("you have indicated MOOD = 1.")
                    mood = 1
            elif(event.key == pygame.K_a):
                if (alert == 1):
                    print("you have indicated ALERTNESS = 0.")
                    alert = 0
                else:
                    print("you have indicated ALERTNESS = 1.")
                    alert = 1
            else:
                print("not a valid key.")
            print("Current alertness (a to switch): " + str(alert))
            print("Current mood (m to switch):      " + str(mood))
            print('Press m to change mood, or a to change alertness.\n')




    
