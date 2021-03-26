import os
import cv2
import numpy as np
import faceRecognition as fr


#This module captures images via webcam and performs face recognition
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('/Users/admin/Downloads/E.D.I.T.H(The virtual assistant)/trainingData.yml')#Load saved training data

name = {0 : "Ankit",1 : "Ayush"}


def call():  

  cap=cv2.VideoCapture(0)
  a = 0
  i = 0
  while a<30:

      a = a + 1
      ret,test_img=cap.read()# captures frame and returns boolean value and captured image
      faces_detected,gray_img=fr.faceDetection(test_img)

      for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

      # resized_img = cv2.resize(test_img, (500, 350))
      # cv2.imshow('face detection',resized_img)
      # cv2.waitKey(10)


      for face in faces_detected:
          (x,y,w,h)=face
          roi_gray=gray_img[y:y+w, x:x+h]
          label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
          print("confidence:",confidence)
          print("label:",label)
          fr.draw_rect(test_img,face)
          predicted_name=name[label]
          if confidence < 32:#If confidence less than 37 then don't print predicted face text on screen
            # fr.put_text(test_img,predicted_name,x,y)
            i = i+1



      # resized_img = cv2.resize(test_img, (500, 350))
      # cv2.imshow('face recognition',resized_img)
      
      if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
          break

      
  cap.release()
  cv2.destroyAllWindows
  if i >= 10:
    return 1
  else:
    return 0

# data = call()
  


