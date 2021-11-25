
# 引入必要的包
import numpy as np
import matplotlib.image as mpimg    # 用于读取
import matplotlib.pyplot as plt     # 用于显示
import logging

class Sharpen(object):
    def __init__(self):
        pass

    def sharpen(img, *, laplacian_type=0,show_laplacian = False):
        size_h, size_w, size_c = img.shape
        # 创建空图像

        new_img = np.zeros([size_h, size_w, size_c], dtype=np.uint8)  # 更改类型
        la_img = np.zeros([size_h, size_w, size_c], dtype=np.uint8)  # 更改类型
        laplacian = [
            [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]],
            [[-1, 0, -1], [0, 4, 0], [-1, 0, -1]],
            [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
        ]
        # laplacian = [[-1, 0, -1], [0, 4, 0], [-1, 0, -1]]
        # laplacian = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
        laplacian = np.asarray(laplacian)
        # 不计算第一行、第一列以及最后一行最后一列，让其保持为 0
        # 注意最后的负数
        for i in range(1, size_h-1):
            for j in range(1, size_w-1):
                location = img[i-1:i+2, j-1:j+2]
                sum = (location * laplacian[laplacian_type]).sum()
                if sum < 0:
                    sum = 0
                la_img[i, j] = sum
                pix_value = min(sum + img[i, j][0], 255)
                new_img[i, j] = pix_value
        if show_laplacian == True:                
            plt.imshow(la_img)
            plt.axis('off')
            plt.show()
        # new_img = la_img + img
        return new_img
    pass  # end class

if __name__ == '__main__':

    pic3 = mpimg.imread('.\hw2_picture3.jpg')

    new_pic_8 = Sharpen.sharpen(pic3,laplacian_type=0)
    new_pic_4 = Sharpen.sharpen(pic3,laplacian_type=2)
    plt.imshow(pic3)
    plt.axis('off')
    plt.show()
    plt.imshow(new_pic_8)
    plt.axis('off')
    plt.show()
    plt.imshow(new_pic_4)
    plt.axis('off')
    plt.show()
    mpimg.imsave(r'.\output_sharpen_8.png', new_pic_8)
    mpimg.imsave(r'.\output_sharpen_4.png', new_pic_4)
