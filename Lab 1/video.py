# Code references: multiple pages linked in the baseline scripts 
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # HSV frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # RGB frame
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # HSV section
    # define range of color in HSV
    lower_blue_hsv = np.array([110,50,50])
    upper_blue_hsv = np.array([130,255,255])
    # threshold the HSV image to get only blue colors in range 
    hsv_mask = cv2.inRange(hsv, lower_blue_hsv, upper_blue_hsv)
    # find HSV contours
    hsv_contours,_ = cv2.findContours(hsv_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_hsv_contour = max(hsv_contours, key=cv2.contourArea, default=None)
    # find and box the largest HSV contour
    if largest_hsv_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_hsv_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('hsv_frame',frame)
    '''
    # RGB section
    # define range of color in HSV
    lower_blue_rgb = np.array([25,25,100])
    upper_blue_rgb = np.array([100,100,255])
    # threshold the HSV image to get only blue colors in range 
    rgb_mask = cv2.inRange(rgb, lower_blue_rgb, upper_blue_rgb)
    # find HSV contours
    rgb_contours,_ = cv2.findContours(rgb_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_rgb_contour = max(rgb_contours, key=cv2.contourArea, default=None)
    # find and box the largest HSV contour
    if largest_rgb_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_rgb_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('rgb_frame',frame)
    '''
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
    
    
    
