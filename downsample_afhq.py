import glob
import os
import cv2
import sys

inp_dir = sys.argv[1]
out_dir = sys.argv[2]
res = int(sys.argv[3])
for f in glob.glob("%s/*/*/*.png" % inp_dir):
    print(f)
    basedir, fname = os.path.split(f)
    filedir = "/".join(basedir.split("/")[1:])
    os.makedirs(os.path.join(out_dir, filedir), exist_ok=True)
    outpath = os.path.join(out_dir, filedir, fname)
    print(basedir, filedir, fname)
    print(outpath)

    img = cv2.imread(f)
    img_res = cv2.resize(img, (res, res))
    print(img.shape, img_res.shape)
    cv2.imwrite(outpath, img_res)
