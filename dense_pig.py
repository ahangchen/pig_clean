from util import read_lines
from PIL import Image
import os
import numpy as np


def high_light():
    test_img_names = read_lines('/hdd/cwh/pigs/test.list')
    all_dir_path = '/hdd/cwh/pigs/all'
    dense_dir_path = '/home/cwh/coding/ccnn'
    high_light_path = 'train_dense_result'
    denses = list()
    dense_names = list()
    for dense_img_name in sorted(os.listdir(dense_dir_path)):
        if 'jpg' in dense_img_name:
            dense_img_path = os.path.join(dense_dir_path, dense_img_name)
            denses.append(np.array(Image.open(dense_img_path), dtype=np.int16))
            dense_names.append(dense_img_name)
    for i, test_img_name in enumerate(sorted(test_img_names)):
        test_img_name = test_img_name.strip()
        test_img_path = os.path.join(all_dir_path, test_img_name)
        im = np.array(Image.open(test_img_path), dtype=np.int16)
        h, w, _ = im.shape
        dim = denses[i]
        dim = dim - 118
        for k in range(h):
            for j in range(w):
                if dim[k, j] > 0:
                    im[k, j, 0] = 0
        # for k in range(h):
        #     for j in range(w):
        #         im[k, j, :] *= dim[k, j] /255.0
        # im[:, :, 0] += dim
        # for j in range(h):
        #     for k in range(w):
        #         im[j, k, 0] = dim[j, k]
        # im[:,:,0] = dim
        im = im.astype(np.uint8)
        Image.fromarray(im).save(os.path.join(high_light_path, dense_names[i]))

if __name__ == '__main__':
    high_light()