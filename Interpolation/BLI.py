# 引入必要的包
import numpy as np
import matplotlib.image as mpimg    # 用于读取
import matplotlib.pyplot as plt     # 用于显示
import logging

from math import ceil


# 双线性插值法
class BLIlinearInterpolation(object):
    def __init__(self,
                 h_rate: float,     # h 的缩放率
                 w_rate: float,     # w 的缩放率
                 *,
                 align='center'
                 ):
        if align not in ['center', 'left']:
            logging.exception(f'{align} is not a valid align parameter')
            align = 'center'
        self.align = align
        self.w_rate = w_rate
        self.h_rate = h_rate
        pass

    def set_rate(self,
                 h_rate: float,      # h 的缩放率
                 w_rate: float     # w 的缩放率
                 ):
        self.w_rate = w_rate
        self.h_rate = h_rate

    # 由变换后的像素坐标得到原图像的坐标    针对高
    def get_src_h(self, dst_i, source_h, goal_h) -> float:
        if self.align == 'left':
            # 左上角对齐
            src_i = float(dst_i * (source_h/goal_h))
        elif self.align == 'center':
            # 将两个图像的几何中心重合。
            src_i = float((dst_i + 0.5) * (source_h/goal_h) - 0.5)
        src_i += 0.001  # 保证为浮点数，是的向上取整和向下取整结果不同
        src_i = max(0.0, src_i)
        src_i = min(float(source_h - 1), src_i)
        return src_i
        pass
    # 由变换后的像素坐标得到原图像的坐标    针对宽

    def get_src_w(self, dst_j, source_w, goal_w) -> float:
        if self.align == 'left':
            # 左上角对齐
            src_j = float(dst_j * (source_w/goal_w))
        elif self.align == 'center':
            # 将两个图像的几何中心重合。
            src_j = float((dst_j + 0.5) * (source_w/goal_w) - 0.5)
        src_j += 0.001  # 保证为浮点数，是的向上取整和向下取整结果不同
        src_j = max(0.0, src_j)
        src_j = min((source_w - 1), src_j)
        return src_j
        pass

    def transform(self, img):

        source_h, source_w, source_c = img.shape  # (235, 234, 3)
        goal_h, goal_w = round(
            source_h * self.h_rate), round(source_w * self.w_rate)
        new_img = np.zeros((goal_h, goal_w, source_c), dtype=np.uint8)

        # print the goal image's shape
        # print(new_img.shape[0], new_img.shape[1])

        # i --> h ,  j --> w
        # x --> w:j  y --> h:i
        for i in range(new_img.shape[0]):       # h
            src_i = self.get_src_h(i, source_h, goal_h)
            for j in range(new_img.shape[1]):
                src_j = self.get_src_w(j, source_w, goal_w)
                i2 = ceil(src_i)
                i1 = int(src_i)
                j2 = ceil(src_j)
                j1 = int(src_j)
                # i 对应 y , j 对应 x
                # x 对应 j , y 对应 i
                x2_x = j2 - src_j
                x_x1 = src_j - j1
                y2_y = i2 - src_i
                y_y1 = src_i - i1
                # print(i,j,src_i,i1,i2,src_j,j1,j2)
                # f(Q_xy) 对应 img[y,x] 即 img[i,j]
                new_img[i, j] = img[i1, j1]*x2_x*y2_y + img[i1, j2] * \
                    x_x1*y2_y + img[i2, j1]*x2_x*y_y1 + img[i2, j2]*x_x1*y_y1

        return new_img

        pass
    pass


# 读取图片并显示
pic1 = mpimg.imread(r'.\hw1_picture1.jpg')
pic2 = mpimg.imread(r'.\hw1_picture2.jpg')
pic3 = mpimg.imread(r'.\hw1_picture3.jpg')

print(pic1.shape)
# Show original image --- hw1_picture1.jpg
# plt.imshow(pic1)
# plt.axis('off')
# plt.show()


# 0.5 缩放
# 0.5 缩放
BLI = BLIlinearInterpolation(0.5, 0.5)

new_pic = BLI.transform(pic1)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_0.5\BLI_0.5pic1.png', new_pic)

new_pic = BLI.transform(pic2)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_0.5\BLI_0.5pic2.png', new_pic)

new_pic = BLI.transform(pic3)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_0.5\BLI_0.5pic3.png', new_pic)


# 3 缩放
BLI = BLIlinearInterpolation(3, 3)

new_pic = BLI.transform(pic1)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_3\BLI_3pic1.png', new_pic)

new_pic = BLI.transform(pic2)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_3\BLI_3pic2.png', new_pic)

new_pic = BLI.transform(pic3)
plt.imshow(new_pic)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\BLI_3\BLI_3pic3.png', new_pic)

print('end')
