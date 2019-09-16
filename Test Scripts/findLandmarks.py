import os
import glob
import cv2
import dlib
import csv
import sys
from itertools import chain 


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

list_of_files = glob.glob('photos/*') 
latest_file = max(list_of_files, key=os.path.getctime)

#files = [x for x in os.listdir("/photos/")
#newest = max(files, key = os.path.getmtime)
#filename = os.fsdecode(newest)

file_path = latest_file

sys.stdout.write('\n\n' + file_path + '\n\n')

img = cv2.imread(file_path, 1)
cv2.imshow('ImageWindow', img)
cv2.waitKey()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces_in_image = detector(img_gray, 0)

landmarks_list = []

for face in faces_in_image:
    sys.stdout.write('\n\n' + "face found" + '\n\n')
    # assign the facial landmarks
    landmarks = predictor(img_gray, face)
    
    # unpack the 68 landmark coordinates from the dlib object into a list 
    for i in range(0, landmarks.num_parts):
      landmarks_list.append((landmarks.part(i).x, landmarks.part(i).y))


landmarks_flattened = list(chain.from_iterable(landmarks_list)) 

# Write landmarks to csv
with open("landmarks.csv", 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(landmarks_flattened)

exit()
