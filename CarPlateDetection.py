import numpy as np
import cv2 as cv
import imutils
import datetime

# TODO: How How ;-)
# All things

class CarPlateDetection:

   def __init__(self):
       self.currentDT = datetime.datetime.now()
       self.image=None
       self.numberPlateCnt = None  # we currently have no Number plate contour

   def __del__(self):
       if not self.image is None:
           print("*******************************")
       # When everything done, release the video capture object
       #self.cap.release()
       # Closes all the frames
       #cv.destroyAllWindows()

   def start(self):
       self.imageRead()
       self.imagesShowMode()
       print("*******************************")
       print("**                             ")
       print("** Start...", self.currentDT)
       print("**                             ")
       print("** ESC - ends app               ")
       print("**                             ")
       while True:
           if cv.waitKey(10) == 27:
               break

   def imageRead(self,fileName='Car_Image_1.jpg'):
       # Read the image file
       self.image = cv.imread(fileName)
       if not self.image is None:
           # Resize the image - change width to 500
           self.image = imutils.resize(self.image, width=500)

   def imagesShowMode(self,mode=0):
       # Display the original image
       cv.imshow("Original Image", self.image)
       # RGB to Gray scale conversion
       gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
       cv.imshow("1 - Grayscale Conversion", gray)
       # Noise removal with iterative bilateral filter(removes noise while preserving edges)
       gray = cv.bilateralFilter(gray, 11, 17, 17)
       cv.imshow("2 - Bilateral Filter", gray)
       # Find Edges of the grayscale image
       edged = cv.Canny(gray, 170, 200)
       cv.imshow("4 - Canny Edges", edged)
       # Find contours based on Edges
       (new, cnts, _) = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
       cnts = sorted(cnts, key=cv.contourArea, reverse=True)[ :30]  # sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
       # loop over our contours to find the best possible approximate contour of number plate
       count = 0
       for c in cnts:
           peri = cv.arcLength(c, True)
           approx = cv.approxPolyDP(c, 0.02 * peri, True)
           if len(approx) == 4:  # Select the contour with 4 corners
               self.numberPlateCnt = approx  # This is our approx Number Plate Contour
               break

       # Drawing the selected contour on the original image
       cv.drawContours(self.image, [self.numberPlateCnt], -1, (0, 255, 0), 3)
       cv.imshow("Final Image With Number Plate Detected", self.image)


# Read the image file
#image = cv2.imread('Car_Image_1.jpg')

# Resize the image - change width to 500
#image = imutils.resize(image, width=500)

# Display the original image
#cv2.imshow("Original Image", image)

# RGB to Gray scale conversion
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("1 - Grayscale Conversion", gray)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
#gray = cv2.bilateralFilter(gray, 11, 17, 17)
#cv2.imshow("2 - Bilateral Filter", gray)

# Find Edges of the grayscale image
#edged = cv2.Canny(gray, 170, 200)
#cv2.imshow("4 - Canny Edges", edged)

# Find contours based on Edges
#(new, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] #sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)


# loop over our contours to find the best possible approximate contour of number plate
#count = 0
#for c in cnts:
#        peri = cv2.arcLength(c, True)
#        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#        if len(approx) == 4:  # Select the contour with 4 corners
#            NumberPlateCnt = approx #This is our approx Number Plate Contour
#            break


# Drawing the selected contour on the original image
#cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)
#cv2.imshow("Final Image With Number Plate Detected", image)

#cv2.waitKey(0) #Wait for user input before closing the images displayed


if __name__=='__main__':
    cpd=CarPlateDetection()
    cpd.start()
