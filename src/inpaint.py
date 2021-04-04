import os
from src.face_recog_test import find_ex
from src.gcp_test import find_human
import numpy as np
import cv2
import time


tmp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../tmp/"))

# Inpainting functions after this line.
# All output files should go to tmp folder using os.path.join(tmp_dir, filename)

def chugjug_with_you(ex_headshot_path, target_img_path):
    im = cv2.imread(target_img_path)

    human_bboxes = find_human(target_img_path)
    human_bboxes_centers = []
    for pair in human_bboxes:
        pair_ = np.array(pair)
        human_bboxes_centers.append((pair_[1]+pair[0])/2)

    ex_face_bbox = find_ex(ex_headshot_path, target_img_path)
    ex_face_bbox_ = np.array(ex_face_bbox)
    ex_face_bbox_center = (ex_face_bbox_[1]+ex_face_bbox_[0])/2

    ex_human_bbox_idx = np.argmin([np.linalg.norm(center-ex_face_bbox_center) for center in human_bboxes_centers])

    ex_bbox = human_bboxes[ex_human_bbox_idx]
    print(ex_bbox)
    # print(human_bboxes_centers)

    inpaint_mask = np.zeros(im.shape[:2], dtype=np.uint8)
    inpaint_mask[ex_bbox[0][1]:ex_bbox[1][1], ex_bbox[0][0]:ex_bbox[1][0]] = 1

    result = cv2.inpaint(im, inpaint_mask, 3, cv2.INPAINT_TELEA)
    # out_impath = tmp_dir + time.strftime("%Y%m%d-%H%M%S") + ".jpg"
    # sorry isaac
    out_impath = "./static/out.jpg"

    cv2.imwrite(out_impath, result)

    return out_impath