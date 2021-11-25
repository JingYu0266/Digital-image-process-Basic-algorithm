

# 引入必要的包
import numpy as np
import matplotlib.image as mpimg    # 用于读取
import matplotlib.pyplot as plt     # 用于显示
import logging




class NearestNeighbourInterpolate(object):
    def __init__(self,
                 w_rate: float,     # w 的缩放率
                 h_rate: float      # h 的缩放率
                 ):
        self.w_rate = w_rate
        self.h_rate = h_rate
        pass

    def set_rate(self,
                 w_rate: float,     # w 的缩放率
                 h_rate: float      # h 的缩放率
                 ):
        self.w_rate = w_rate
        self.h_rate = h_rate

    def transform(self, img):
        source_h, source_w, source_c = img.shape  # (235, 234, 3)
        goal_h, goal_w = round(source_h * self.h_rate), round(source_w * self.w_rate)
        new_img = np.zeros((goal_h, goal_w, source_c), dtype=np.uint8)

        print(new_img.shape[0], new_img.shape[1])

        for i in range(new_img.shape[0]):       # h
            for j in range(new_img.shape[1]):   # w  img[h,w] , new_img[h,w]
                new_img[i, j] = img[round(
                    (source_h-1) * i / new_img.shape[0]), round((source_w-1) * j / new_img.shape[1])]
        return new_img


        
    pass

pic1 = mpimg.imread('./hw1_picture1.jpg')
pic2 = mpimg.imread('./hw1_picture2.jpg')
pic3 = mpimg.imread('./hw1_picture3.jpg')

# 0.5 倍缩放
NNI = NearestNeighbourInterpolate(0.5,0.5)

new_pic1_half =  NNI.transform(pic1)
plt.imshow(new_pic1_half)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\NNI_0.5\NNI_0.5pic1.png',new_pic1_half)

new_pic1_half =  NNI.transform(pic2)
plt.imshow(new_pic1_half)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\NNI_0.5\NNI_0.5pic2.png',new_pic1_half)

new_pic1_half =  NNI.transform(pic3)
plt.imshow(new_pic1_half)
plt.axis('off')
plt.show()
mpimg.imsave(r'.\NNI_0.5\NNI_0.5pic3.png',new_pic1_half)

# 3 倍缩放
# NNI = NearestNeighbourInterpolate(3,3)

# new_pic =  NNI.transform(pic1)
# plt.imshow(new_pic)
# plt.axis('off')
# plt.show()
# mpimg.imsave(r'.\NNI_3\NNI_3pic1.png',new_pic)

# new_pic =  NNI.transform(pic2)
# plt.imshow(new_pic)
# plt.axis('off')
# plt.show()
# mpimg.imsave(r'.\NNI_3\NNI_3pic2.png',new_pic)

# new_pic =  NNI.transform(pic3)
# plt.imshow(new_pic)
# plt.axis('off')
# plt.show()
# mpimg.imsave(r'.\NNI_3\NNI_3pic3.png',new_pic)
