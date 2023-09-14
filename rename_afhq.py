import os
import sys
import glob

classes = ["cat", "dog", "wild"]
inp_dir = sys.argv[1]
rename = len(sys.argv) > 2 and str(sys.argv[2]).lower() == "true"
for f in glob.glob("%s/*/*/*.png" % inp_dir):
    file_dir, file_name = os.path.split(f)
    label = file_dir.split("/")[-1]
    assert label in classes
    new_file_name = "_".join([label, file_name.split("_")[-1]])
    newf = os.path.join(file_dir, new_file_name)
    print(f, newf)
    if rename:
        os.rename(f, newf)
