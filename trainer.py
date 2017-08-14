import os  # importing the OS for path
import cv2  # importing the OpenCV library
import numpy as np  # importing Numpy library
from PIL import Image  # importing Image library


class Trainer:
    def __init__(self):
        LBPHFace = cv2.face.createLBPHFaceRecognizer(1, 1, 7, 7)

        if not os.path.exists('Recogniser'):
            os.makedirs('Recogniser')

        path = 'dataSet'  # path to the photos

        def getImageWithID(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            FaceList = []
            IDs = []
            for imagePath in imagePaths:
                faceImage = Image.open(imagePath).convert('L')
                faceImage = faceImage.resize((110, 110))
                faceNP = np.array(faceImage, 'uint8')
                ID = int(os.path.split(imagePath)[-1].split('.')[1])
                FaceList.append(faceNP)
                IDs.append(ID)
                cv2.imshow('Training Set', faceNP)
                cv2.waitKey(1)
            return np.array(IDs), FaceList

        IDs, FaceList = getImageWithID(path)

        # ------------------------------------ TRAINING THE RECOGNISER ----------------------------------------
        print('TRAINING......')
        LBPHFace.train(FaceList, IDs)
        print('LBPH FACE RECOGNISER COMPLETE...')
        LBPHFace.save('Recogniser/trainingDataLBPH.xml')
        print ('ALL XML FILES SAVED...')

        cv2.destroyAllWindows()
