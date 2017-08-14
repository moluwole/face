import cv2
import NameFind
import numpy as np


class Getface:

    def __init__(self, name):
        print name
        face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
        eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)
        print cap.isOpened()

        if cap.isOpened():

            while True:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    gray_face = cv2.resize((gray[y: y + h, x: x + w]), (110, 110))
                    eyes = eye_cascade.detectMultiScale(gray_face)
                    for (ex, ey, ew, eh) in eyes:
                        NameFind.draw_box(gray, x, y, w, h)

                cv2.imshow("Face Detection Using Haar-Cascades ", gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

# face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
# eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
#
# cap = cv2.VideoCapture(0)
# print cap.isOpened()
#
# if cap.isOpened():
#
#     while True:
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
#
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for(x, y, w, h) in faces:
#             gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))
#             eyes = eye_cascade.detectMultiScale(gray_face)
#             for(ex, ey, ew, eh) in eyes:
#                 NameFind.draw_box(gray, x, y, w, h)
#
#         cv2.imshow("Face Detection Using Haar-Cascades ", gray)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# cap.release()
# cv2.destroyAllWindows()
