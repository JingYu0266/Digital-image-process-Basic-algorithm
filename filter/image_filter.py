# 引入必要的包
import numpy as np
import matplotlib.image as mpimg    # 用于读取
import matplotlib.pyplot as plt     # 用于显示
import logging







class MeanFilter(object):
    def __init__(self):
        # super.__init__(self, t, obj)
        pass
    # @staticmethod
    def _filter(img):
        size_h, size_w, size_c = img.shape

        new_img = np.zeros([size_h, size_w, size_c], dtype=np.uint8)

        for i in range(size_h):

            for j in range(size_w):
                sum = np.zeros([1,3],dtype = np.uint32)
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if i+x < 0 or i+x >= size_h or j+y < 0 or j+y >= size_w:
                            continue
                        # print(i+x,j+y,img[i+x, j+y])
                        sum += img[i+x, j+y]
                        # print(sum)
                        count += 1
                    
                # print(img[i,j],sum,count,sum/count)
                new_img[i, j] = sum/count
                # print(new_img[i,j])
        return new_img
    # time 控制滤波次数 ，均值滤波经过实验 ，1次即可，再多会影响图像的质量（变很模糊）
    def filter(img ,*, time = 1):
        for i in range(time):
            img = MeanFilter._filter(img)
        return img
    pass






class MedianFilter(object):
    def __init__(self):
        pass

    def _filter(img):
        size_h, size_w, size_c = img.shape

        new_img = np.zeros([size_h, size_w, size_c], dtype=np.uint8)

        for i in range(size_h):
            for j in range(size_w):
                # 对于滤波后图像的每一个像素点
                # sum = np.zeros([1,3],dtype = np.uint32)
                temp = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        # 越界的像素点不考虑
                        if i+x < 0 or i+x >= size_h or j+y < 0 or j+y >= size_w:
                            continue
                        temp.append(img[i+x,j+y])       
                median = int(np.median(temp))
                new_img[i, j] = np.asarray([median,median,median])
                del temp
                # print(new_img[i,j])
        return new_img
    # time 控制滤波次数 
    def filter(img ,*, time = 2):
        for i in range(time):
            img = MedianFilter._filter(img)
        return img
    

    pass



if __name__ == '__main__':
        
    pic2 = mpimg.imread('.\hw2_picture2.jpg')

    plt.imshow(pic2)
    plt.axis('off')
    plt.show()

    new_pic = MeanFilter.filter(pic2)
    plt.imshow(new_pic)
    plt.axis('off')
    plt.show()
    # mpimg.imsave(f'.\mean_filter_output\output_mean_filter.png',new_pic)
    mpimg.imsave(f'.\output_mean_filter.png',new_pic)


    new_pic = MedianFilter.filter(pic2,time=2)
    plt.imshow(new_pic)
    plt.axis('off')
    plt.show()
    # mpimg.imsave(r'.\median_filter_output\output_median_filter.png',new_pic)
    mpimg.imsave(r'.\output_median_filter.png',new_pic)

print('end')