import cv2
import numpy as np
import NameFind

class FaceCapture:
    def __init__(self, name):
        WHITE = [255, 255, 255]

        face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
        eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

        ID = NameFind.AddName(name)
        Count = 0
        cap = cv2.VideoCapture(0)  # Camera object

        while Count < 50:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the Camera to grayScale
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect the faces and store the positions
            for (x, y, w, h) in faces:  # Frames  LOCATION X, Y  WIDTH, HEIGHT
                FaceImage = gray[y - int(h / 2): y + int(h * 1.5),
                            x - int(x / 2): x + int(w * 1.5)]  # The Face is isolated and cropped
                Img = (NameFind.DetectEyes(FaceImage))
                cv2.putText(gray, "FACE DETECTED", (x + (w / 2), y - 5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
                if Img is not None:
                    frame = Img  # Show the detected faces
                else:
                    frame = gray[y: y + h, x: x + w]
                cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
                # cv2.waitKey(300)
                cv2.imshow("CAPTURED PHOTO", frame)  # show the captured image
            Count = Count + 1
            cv2.imshow('Face Recognition System Capture Faces', gray)  # Show the video
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        print 'FACE CAPTURE FOR THE SUBJECT IS COMPLETE'
        cap.release()
        cv2.destroyAllWindows()


# WHITE = [255, 255, 255]
#
# face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
# eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
#
# ID = NameFind.AddName()
# Count = 0
# cap = cv2.VideoCapture(0)  # Camera object
#
# while Count < 50:
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the Camera to grayScale
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect the faces and store the positions
#     for (x, y, w, h) in faces:  # Frames  LOCATION X, Y  WIDTH, HEIGHT
#         FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]  # The Face is isolated and cropped
#         Img = (NameFind.DetectEyes(FaceImage))
#         cv2.putText(gray, "FACE DETECTED", (x + (w / 2), y - 5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
#         if Img is not None:
#             frame = Img  # Show the detected faces
#         else:
#             frame = gray[y: y + h, x: x + w]
#         cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
#         # cv2.waitKey(300)
#         cv2.imshow("CAPTURED PHOTO", frame)  # show the captured image
#     Count = Count + 1
#     cv2.imshow('Face Recognition System Capture Faces', gray)  # Show the video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# print 'FACE CAPTURE FOR THE SUBJECT IS COMPLETE'
# cap.release()
# cv2.destroyAllWindows()
