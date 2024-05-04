import os
import cv2 as cv
import numpy as np

# people= ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
Dir = r'D:\Files\Ayush\document and educational\CS\practice_page\page42(Opencv)\Faces\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')
p  =[]
for i in os.listdir(Dir):
    p.append(i)
# print(p)
features = []
labels = []

def create_train():
    for person in p:
        path= os.path.join(Dir, person)
        label = p.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array =  cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print("Training Done ------------------------")

features = np.array(features, dtype='object')
labels = np.array(labels)

# print(f"Length of the features = {len(features)}")
# print(f"Length of the labels = {len(labels)}")  

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save("Features.npy", features)
np.save("labels.npy", labels)
