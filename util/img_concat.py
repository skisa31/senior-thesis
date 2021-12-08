from glob import glob
import cv2
import numpy as np
import pandas as pd
# np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

dir_name = input("input path (name) : ")
dir_path = glob("./slidebar_img/{}/test*".format(dir_name))
count = 0

for d in dir_path:
    count += 1
    input_files = glob("{}/*.png".format(d))
    imgs_arr = np.array([cv2.imread(p) for p in sorted(input_files)])
    imgs_arr2 = np.array([imgs_arr[:, 1, :, 0]])
    concat_img = cv2.vconcat(imgs_arr2)
    ret, img_th = cv2.threshold(concat_img, 127, 255, cv2.THRESH_BINARY)
    print(np.shape(img_th))
    """
    全部表示するときは20までコメントアウト
    """
    for i, p in enumerate(img_th):
        if np.count_nonzero(p == 0) > 6 :
            p = np.where(p == 0, -1, 255)
        else:
            pass

    df = pd.DataFrame(img_th)
    df.replace(-1, np.nan, inplace=True)
    """
    with open('./test{}.txt'.format(count), 'w', encoding='utf-8') as fw :
        fw.writelines(str(df))
    """
    filled_df = df.interpolate(limit_direction='both')
    print(filled_df.head())
    filled_img = np.array([filled_df.values])
    print(np.shape(filled_img))
    cv2.imwrite("./slidebar_img/{}/merged_test{}.png".format(dir_name, count), filled_img[0])
    print("completed {} file".format(count))
