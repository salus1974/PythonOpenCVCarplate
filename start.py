import cv2 as cv
from kamera import  Kamera
from CarPlateDetection import CarPlateDetection
import time

class Goo(object):

    def __init__(self):

        self.cpd = CarPlateDetection()


        self.camera = Kamera()
        self.frame=None

    def execute(self):
        while True:
            #time.sleep(0.5)
            self.frame=self.camera.captureFrame()
            if self.frame is None:
                print('-- (!) No captured frame -- Break!')
                break
            else:
                # Display the resulting frame
                cv.imshow('Frame', self.frame)
                self.cpd.procImage(self.frame)
            if cv.waitKey(10) == 27:
                break


if __name__=='__main__':
    print("Start z opencv...", cv.__version__)



    go=Goo()
    go.execute()












