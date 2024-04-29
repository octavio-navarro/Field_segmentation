import cv2
import numpy as np
import pandas as pd
import os, glob

DATA_PATH = '../data/images'
CLASSES_PATH = '../data/class_dict.csv'
META_PATH = '../data/meta.csv'

images = glob.glob(f'{DATA_PATH}/*sat*')
masks = glob.glob(f'{DATA_PATH}/*mask*')

images.sort()
masks.sort()

classes = pd.read_csv(CLASSES_PATH)
meta = pd.DataFrame(columns=['image_path', 'mask_path', 'mask_classes'])

for image_path, mask_path in zip(images, masks):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

    mask = cv2.resize(mask, (256, 256), interpolation=cv2.INTER_NEAREST)

    h, w, c = mask.shape

    mask = np.reshape(mask, (h*w, c))

    mask_colors = np.unique(mask, axis=0)
    mask_classes = []

    for color in mask_colors.tolist():
        r, g, b = color
        mask_classes.append(classes[(classes['r'] == r) & (classes['g'] == g) & (classes['b'] == b)].index.values[0])

    data = {
        'image_path': image_path,
        'mask_path': mask_path,
        'mask_classes': mask_classes
    }
    meta = meta._append(data, ignore_index=True)

meta.to_csv(META_PATH, index=False)
