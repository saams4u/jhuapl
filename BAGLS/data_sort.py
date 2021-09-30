from pathlib import Path
import os

import shutil

TRAINING_PATH = "datasets/Images/training/"
TEST_PATH = "datasets/Images/test/"

TRAIN_ANNOTATIONS_PATH = "datasets/Labels/training/"
TEST_ANNOTATIONS_PATH = "datasets/Labels/test/"

MODELS_PATH = Path("models/")

N_train = 55750 
N_test = 3500

# All training images
train_imgs = [TRAINING_PATH + str(i) + ".png" for i in range(N_train)]
train_segs = [TRAINING_PATH + str(i) + "_seg.png" for i in range(N_train)]

# All test images
test_imgs = [TEST_PATH + str(i) + ".png" for i in range(N_test)]
test_segs = [TEST_PATH + str(i) + "_seg.png" for i in range(N_test)]

for item in train_segs:
    shutil.move(item, TRAIN_ANNOTATIONS_PATH)

for item in test_segs:
    shutil.move(item, TEST_ANNOTATIONS_PATH)
    
train_annot_segs = [TRAIN_ANNOTATIONS_PATH + str(i) + "_seg.png" for i in range(N_train)]
test_annot_segs = [TEST_ANNOTATIONS_PATH + str(i) + "_seg.png" for i in range(N_test)]

suffix = '_seg'

for item in train_annot_segs:
    os.rename(item, item.replace(suffix, ''))

for item in test_annot_segs:
    os.rename(item, item.replace(suffix, ''))
    
from glob import glob

TRAINSET_SIZE = len(glob(TRAINING_PATH + "*.png"))
print(f"The Training Dataset contains {TRAINSET_SIZE} images.")

VALSET_SIZE = len(glob(TEST_PATH + "*.png"))
print(f"The Validation Dataset contains {VALSET_SIZE} images.")