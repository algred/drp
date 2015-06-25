import cv2
import numpy as np

def read_video(vfile):
    cap = cv2.VideoCapture(vfile)
    ind = 0
    frames = []
    while(True):
        ret, frame = cap.read()
        if not ret:
#             print "Finish reading " + vfile + \
#                     ": " + str(ind) + " frames."
            break
        frames.append(frame)
        ind = ind + 1

    cap.release()
    return frames

