import numpy as np
import cv2
import glob
import os
import json

# data = json.loads(open('activity_net.json').read())
# data = data['database']

video_root = "/data/shugao/ActivityNet"
video_files = glob.glob(video_root + "/*.mp4")
image_root = "/data/shugao/ActivityNetImg"
video_files = video_files[0:1]

for vfile in video_files:
    vpath, vname = os.path.split(vfile)
    vinfo = data[vname[:-4]]

    image_path = image_root + "/" + vname[:-4]
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    cap = cv2.VideoCapture(vfile)
    ind = 0
    while(True):
        ret, frame = cap.read()
        if not ret:
            print "Finish reading " + vfile + \
                    ": " + str(ind) + " frames."
            break
        image_name = "%06d.jpg" % ind
        cv2.imwrite(image_path + "/" + image_name, frame,
                [cv2.IMWRITE_JPEG_QUALITY, 80])
        ind = ind + 1


    cap.release()

