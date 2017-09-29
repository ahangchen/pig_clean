import os
import shutil
from PIL import Image
import numpy as np
import scipy.misc as sm


def rename():
    im_cnt = 1
    all_path = '/hdd/cwh/pigs/all'
    for i in [1, 2, 3, 4]:
        dir_path = '/hdd/cwh/pigs/%d' % i
        for file_name in sorted(os.listdir(dir_path)):
            if 'txt' not in file_name and 'py' not in file_name:
                shutil.copy(os.path.join(dir_path, file_name), os.path.join(all_path, str(im_cnt) + '.' + (file_name.split('.')[1])))
                shutil.copy(os.path.join(dir_path, file_name.split('.')[0] + '.txt'), os.path.join(all_path, str(im_cnt) + '.txt'))
                im_cnt += 1


def del_reformat():
    for i in [3]:
        dir_path = '/hdd/cwh/pigs/%d' % i
        for file_name in sorted(os.listdir(dir_path)):
            if 'txt' in file_name:
                pos = np.genfromtxt(os.path.join(dir_path, file_name), delimiter=' ')
                np.savetxt(os.path.join(dir_path, file_name), pos, fmt='%d', delimiter='\t')


def dot_img():
    all_dir_path = '/hdd/cwh/pigs/all'
    for file_name in sorted((os.listdir(all_dir_path))):
        if 'txt' not in file_name and 'py' not in file_name:
            name = file_name.split('.')[0]
            dots = np.genfromtxt(os.path.join(all_dir_path, name) + '.txt', delimiter='\t')
            file_path = os.path.join(all_dir_path, file_name)
            origin_img = Image.open(file_path)
            size = origin_img.size
            empty_img = np.zeros((640, 641, 3), np.uint8)
            print file_name
            if len(dots.shape) > 1:
                for dot in dots:
                    empty_img[int(dot[1]/size[1]*640), int(dot[0]/size[0]*641)][0] = 255
            else:
                empty_img[int(dot[1]/size[1]*640), int(dot[0]/size[0]*641)][0] = 255
            im = Image.fromarray(empty_img)
            im.save(os.path.join(all_dir_path, name + 'dots.png'))
            origin_img.resize([641, 640]).save(os.path.join(all_dir_path, file_name))


def read_dot_png():
    all_dir_path = '/hdd/cwh/pigs/all'
    im = Image.open(os.path.join(all_dir_path, '1dots.png'))
    size = im.size


if __name__ == '__main__':
    # del_reformat()
    # rename()
    dot_img()
    read_dot_png()