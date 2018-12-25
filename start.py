import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
args = parser.parse_args()

camera_device = args.camera

#-- 2. Read the video stream

cap = cv.VideoCapture(camera_device)

if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
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



print( "Start z opencv...", cv.__version__)


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv.destroyAllWindows()