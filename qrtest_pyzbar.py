#import required libraries
from imutils.video import VideoStream
from pyzbar import pyzbar
import numpy
import argparse
import datetime
import imutils
import time
import cv2

#start video stream, with samll delay to allow camera to warm up
print("video stream starting")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

#will loop until exit key is pressed
while True:
    frame = vs.read() #read frame data from video stream
    
    frame = imutils.resize(frame, width=250) #normalize frame data
    barcodes = pyzbar.decode(frame) #pyzbar to decode QR code
    
    for barcode in barcodes: #pyzbar gives a python list, this iterates through all elements (found QR codes)
        bcd = barcode.data.decode("utf-8") #converts data in barcode function to usable text
        bct = barcode.type #pyzbar built in object method to get type
        print("found {} code: {}".format(bct,bcd)) #print the found data
        
        #use opencv to make a nice border and text around QR code
        (x,y,w,h) = barcode.rect
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),2)
        text = "{}({})".format(bcd,bct)
        cv2.putText(frame, text, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    #show the live feed and clean up memory when 'q' is pressed, otherwise loop infinitly
    
    cv2.imshow("Scanner view", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
print("exiting")
cv2.Close()
cv2.destroyAllWindows()
vs.stop()
