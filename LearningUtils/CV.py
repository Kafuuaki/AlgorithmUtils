import cv2
import numpy as np
import time
from typing import NoReturn

import os


def crop3_Iter(source_path: str, save_path: str) -> NoReturn:
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    file_name: str = os.listdir(source_path)
    # print(file_name)

    for i in range(len(file_name)):
        img: np.ndarray = cv2.imread(os.path.join(source_path, file_name[i]))

        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # exit(0)

        height, width, _ = img.shape
        crop_height = height//3
        sub_img1 = img[:crop_height, :]
        sub_img2 = img[crop_height: 2*crop_height, :]
        sub_img3 = img[2*crop_height:3*crop_height, :]

        assert sub_img1.shape == sub_img2.shape == sub_img3.shape

        cv2.imwrite(os.path.join(save_path, 'crop_' +
                    file_name[i].replace('.jpg', '_01.jpg')), sub_img1)
        cv2.imwrite(os.path.join(save_path, 'crop_' +
                    file_name[i].replace('.jpg', '_02.jpg')), sub_img2)
        cv2.imwrite(os.path.join(save_path, 'crop_' +
                    file_name[i].replace('.jpg', '_03.jpg')), sub_img3)


img1: np.ndarray = cv2.imread('./data/1.jpg')

# crop3(img1, './')
# img2: np.ndarray = cv2.imread(
#     '/Users/yejianqiu/Desktop/Reading/Slam/data/2.jpg')
# img3: np.ndarray = cv2.imread(
#     '/Users/yejianqiu/Desktop/Reading/Slam/data/3.jpg')
# img4: np.ndarray = cv2.imread(
#     '/Users/yejianqiu/Desktop/Reading/Slam/data/4.jpg')
# img5: np.ndarray = cv2.imread(
#     '/Users/yejianqiu/Desktop/Reading/Slam/data/5.jpg')
# img6: np.ndarray = cv2.imread(
#     '/Users/yejianqiu/Desktop/Reading/Slam/data/6.jpg')

# what does it mean image with shape (480, 640, 3)?
# 480 is the height, 640 is the width, 3 is the channel


# import cv2
# import os
# import datetime


# def change_size(read_file):
#     image = cv2.imread(read_file, 1)  # 读取图片 image_name应该是变量
#     img = cv2.medianBlur(image, 5)  # 中值滤波，去除黑色边际中可能含有的噪声干扰
#     b = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)  # 调整裁剪效果
#     binary_image = b[1]  # 二值图--具有三通道
#     binary_image = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)
#     print(binary_image.shape)  # 改为单通道

#     x = binary_image.shape[0]
#     print("高度x=", x)
#     y = binary_image.shape[1]
#     print("宽度y=", y)
#     edges_x = []
#     edges_y = []
#     for i in range(x):
#         for j in range(y):
#             if binary_image[i][j] == 255:
#                 edges_x.append(i)
#                 edges_y.append(j)

#     left = min(edges_x)  # 左边界
#     right = max(edges_x)  # 右边界
#     width = right-left  # 宽度
#     bottom = min(edges_y)  # 底部
#     top = max(edges_y)  # 顶部
#     height = top-bottom  # 高度

#     pre1_picture = image[left:left+width, bottom:bottom+height]  # 图片截取
#     return pre1_picture  # 返回图片数据


# # source_path = "01.jpg"  # 图片来源路径
# # save_path = "./out/"  # 图片修改后的保存路径

# # if not os.path.exists(save_path):
# #     os.mkdir(save_path)

# # file_names = os.listdir(source_path)

# # starttime = datetime.datetime.now()
# # for i in range(len(file_names)):
# x = change_size("01.jpg")  # 得到文件名
# cv2.imshow("cut", x)
# cv2.waitKey()

# cv2.imwrite, ("cut")
# # print("裁剪：", file_names[i])
# # print("裁剪数量:", i)
# # while (i == 2600):
# #     break
# print("裁剪完毕")
# endtime = datetime.datetime.now()  # 记录结束时间
# # endtime = (endtime-starttime).seconds
# # print("裁剪总用时", endtime)


if __name__ == "__main__":
    crop3_Iter('./data/source', './data/cropped')
    pass
