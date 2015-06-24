import numpy as np
import cv2
import glob
import os
import json

action_class = json.loads(open('action_class.json').read())
data = json.loads(open('activity_net.json').read())
data = data['database']

video_root = "/data/shugao/ActivityNet"
video_files = glob.glob(video_root + "/*.mp4")
train_img_root = "/data/shugao/ActivityNetTrainImg"
val_img_root = "/data/shugao/ActivityNetValImg"
video_files = video_files[0:1]

for vfile in video_files:
  vpath, vname = os.path.split(vfile)
  vinfo = data[vname[:-4]]

  # Reads all frames into memory.
  cap = cv2.VideoCapture(vfile)
  ind = 0
  while(True):
      ret, frame = cap.read()
      if not ret:
          print "Finish reading " + vfile + \
                  ": " + str(ind) + " frames."
          break
      frames[ind] = frame
      ind = ind + 1

  # Writes frames of annotated actions.
  if vinfo['subset'] == 'training':
    image_root = train_img_root
  elif vinfo['subset'] == 'validation':
    image_root = val_img_root
  else
    continue

  actions = vinfo['annotations']
  for action in actions
    action_label = action_class[action]
    annot = actions[action]
    for a in annot

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

