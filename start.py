import cv2 as cv
import argparse

class Kamera(object):

    def __init__(self):
        self.parser=None
        self.args=None
        self.camera_device=None
        self.cap=None
        self.argument()
        self.create_capture()

    def __del__(self):
        if not self.cap is None:
            # When everything done, release the video capture object
            self.cap.release()
        # Closes all the frames
        cv.destroyAllWindows()

    def argument(self):
        self.parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
        self.parser.add_argument('--face_cascade', help='Path to face cascade.',
                            default='data/haarcascades/haarcascade_frontalface_alt.xml')
        self.parser.add_argument('--eyes_cascade', help='Path to eyes cascade.',
                            default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
        self.parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
        self.args = self.parser.parse_args()
        if self.args is None:
            print("ArgumentParser error..")
            exit(0)
        else:
            self.camera_device = self.args.camera

    def create_capture(self):
        # -- 2. Read the video stream
        self.cap = cv.VideoCapture(self.camera_device)
        if not self.cap.isOpened:
            print('--(!)Error opening video capture')
            exit(0)


    def run(self):
        while True:
            if self.cap is None:
                print('-- (!) No captured frame -- Break!')
            else:
                ret, frame = self.cap.read()
                if frame is None:
                    print('-- (!) No captured frame -- Break!')
                    break
                else:
                    # Display the resulting frame
                    cv.imshow('Frame', frame)
                    #print('-- jest ok..')
                    #detectAndDisplay(frame)
            if cv.waitKey(10) == 27:
                break


if __name__=='__main__':
    print("Start z opencv...", cv.__version__)

    kamera=Kamera()
    kamera.run()









