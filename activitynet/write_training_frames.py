import numpy as np
import math
import glob
import os
import json
import threading
from write_frames import write_frames

def worker(first_vid, last_vid, tid):
    action_class = json.loads(open('action_class.json').read())
    data = json.loads(open('activity_net.json').read())
    data = data['database']

    video_root = "/data/shugao/ActivityNet"
    video_files = glob.glob(video_root + "/*.mp4")
    train_img_root = "/data/shugao/ActivityNetTrainImg"
    val_img_root = "/data/shugao/ActivityNetValImg"

    video_files = video_files[first_vid : last_vid]
    for vfile in video_files:
        vpath, vname = os.path.split(vfile)
        vinfo = data[vname[:-4]]

        if vinfo['subset'] == 'training':
            image_root = train_img_root
        elif vinfo['subset'] == 'validation':
            image_root = val_img_root
        else:
            continue
        write_frames(vfile, vinfo, image_root, action_class)
        print "[TID = %d]" % tid


video_root = "/data/shugao/ActivityNet"
video_files = glob.glob(video_root + "/*.mp4")
threads = []
num_threads = 10
num_videos = len(video_files)
batch_size = int(math.ceil(num_videos / num_threads))
for i in range(num_threads):
    vid1 = i * batch_size
    vid2 = min(num_videos - 1, vid1 + batch_size - 1)
    t = threading.Thread(target=worker, args=(vid1, vid2, i, ))
    t.start()
    threads.append(t)
