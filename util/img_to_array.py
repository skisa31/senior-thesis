from os.path import dirname
import cv2
import numpy as np
from glob import glob
import os

dir_name = input("input path (name) : ")
dir_path = glob("./slidebar_img/{}/test*".format(dir_name))
count = 0

for d in dir_path:
    input_files = glob("{}/*.png".format(d))
    count += 1
    slide_num = []
    output_path = "./slidebar_img/{}/slide_score{}.txt".format(dir_name, count)
    with open(output_path, "w", encoding="utf=8") as fw:
        count2 = 0
        for i in input_files:
            count2 += 1
            slide_val = []

            img = cv2.imread(i)
            ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

            val_arr = np.array(th[1, :, 0])
            val_arr = np.append(val_arr, [255, 255])
            val_arr = val_arr.reshape(6, -1)
            val_arr = np.where(val_arr == 0, 1, 0)

            for i in range(val_arr.shape[0]):
                if val_arr[i].sum() >= 6:
                    slide_val.append(1)
                else:
                    slide_val.append(0)
            if sum(slide_val) >= 2:
                print("mistake calc score in line {}".format(count2))
            # print(slide_val)
            if 1 in slide_val:
                slide_num.append(2 * slide_val.index(1))
            else:
                slide_num.append(0)
        for i in slide_num[::10]:
            fw.writelines("{}\n".format(i))
    print("complete {} file".format(count))
