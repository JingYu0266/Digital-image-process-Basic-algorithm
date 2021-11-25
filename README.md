# Digital-image-process-Basic-algorithm
These are some basic algorithms that I have implemented by my hands in the process of learning digital image processing, such as mean and median filtering, sharpening algorithms, interpolation scaling algorithms, histogram equalization algorithms, etc.



文件目录：

- filter : 滤波，代码都在 `image_filter.py`中，目前有
  - 均值滤波
  - 中值滤波
  
- sharpen: 锐化，现在只有基于 拉普拉斯算子的锐化算法。

- Interpolation: 内插，用于图像的缩放，目前有

  - 最近邻内插 - `NNI.py`

  - 双线性内插 - `BLI.py`

  - 双立方内插（双三次内插）- `BCI.py`
- Histogram equalization：直方图均衡化 - `image_HE.py`

