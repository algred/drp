import numpy as np
import random
import os
import cv2
from video_utils import read_video

def write_frames(vfile, vinfo, image_root, action_class):
    IMG_DIM = 256
    TIME_STEP = 5
    K = 200

    vpath, vname = os.path.split(vfile)

    # Reads all frames into memory.
    frames = read_video(vfile)
    nfms = len(frames)
    mask = np.ones(nfms, dtype=bool)

    # Writes frames of annotated actions.
    actions = vinfo['annotations']
    for action in actions:
        action_label = action_class[action]
        annot = actions[action]
        image_path = image_root + "/" + str(action_label) \
                + "/" + vname[:-4] + "/"
        if not os.path.exists(image_path):
            os.makedirs(image_path)

        for a in annot:
            s1 = min(int(a[0]), nfms)
            s2 = min(int(a[1]), nfms)
            mask[range(s1 - 1, s2 - 1)] = False
            for idx in range(s1, s2, TIME_STEP):
                image_name = "%06d.jpg" % idx
                img = cv2.resize(frames[idx-1], (IMG_DIM, IMG_DIM))
                cv2.imwrite(image_path + image_name, img,
                        [cv2.IMWRITE_JPEG_QUALITY, 90])

    # Writes irrelevant frames for use as negative sample.
    irlvt_idx = np.where(mask)
    irlvt_idx = irlvt_idx[0]
    sampled_idx = random.sample(irlvt_idx, min(K, len(irlvt_idx)))
    image_path = image_root + "/" + str(len(action_class) + 1) + \
        "/" + vname[:-4]
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    for idx in sampled_idx:
        image_name = "%06d.jpg" % idx
        img = cv2.resize(frames[idx-1], (IMG_DIM, IMG_DIM))
        cv2.imwrite(image_path + "/" + image_name, img,
                [cv2.IMWRITE_JPEG_QUALITY, 90])


    print "Finshed writing frames for %s." % vname





