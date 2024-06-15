# Image Colorization
Student Name: Chen Sunbing, Chen Tianle, Nian Ziyao, Wu Jixuan

Student ID: 12011118, 12012304, 12011925, 12012301 

## 1. Introduction
图像上色是计算机视觉中的一个重要任务，它旨在为灰度图像自动添加逼真的颜色。这个任务不仅在学术研究中引起了广泛关注，在实际应用中也具有重要意义。例如，通过图像上色技术，我们可以为历史黑白照片上色，使它们重新焕发光彩，帮助人们更好地理解和感受历史。此外，这项技术在电影修复、图像增强和虚拟现实等领域也有广泛的应用。

图像上色的挑战在于颜色信息在灰度图像中是缺失的，模型需要从图像的内容和上下文中推断出合适的颜色。这涉及到对物体、场景以及语义信息的深刻理解。例如，一棵树应该是绿色的，而天空应该是蓝色的。这不仅需要模型具备强大的特征提取能力，还需要对颜色选择有一定的直觉和判断。

近年来，随着深度学习的迅速发展，特别是卷积神经网络（CNN）和生成对抗网络（GAN）的引入，图像上色技术取得了显著进展。基于深度学习的方法可以从大规模数据集中学习颜色和灰度图像之间的复杂关系，从而实现高质量的图像上色。

本项目基于开源仓库DeOldify，实现了对黑白图片的自动上色。我们在原有代码基础上，通过Flask构建了一个轻量化的后端API，并使用Vue框架开发了一个美观易用的前端页面，方便用户进行交互和使用。


## 2. Related Works

Briefly introduce the related works that have been proposed.


## 3. Method

Two options:

-   If you propose your own methods, describe them here.
-   If you are using methods that have been proposed, introduce the method in your own words (do not copy & paste from the paper). A citation to the original paper is needed. Alternatively, if you've made some improvements, highlight and state them here.

## 4. Experiments

#### 4.1 Datasets

本文训练所使用的数据集来源于Kaggle和modelscope，包含三个数据集，kaggl——flowers-recognition; modelscope——flower; modelscope——dailytags。

其中kaggl——flowers-recognition是一个经典的花卉识别数据集，包含了五种不同种类的花朵图像，分别是雏菊、蒲公英、玫瑰、向日葵和郁金香。每个类别平均有大约800张图片。

modelscope——flower是一个更为综合的花卉图像数据集，涵盖了更多种类的花朵，并且每种花朵的图像也更多样化，包含了不同的拍摄角度、光照条件和背景。一共包含了14类花朵，每一类平均有大约950张图片。

 modelscope——dailytags主要包含了日常生活中常见的物体以及对应的物品标签，共包含124张图片，在本文的训练数据中不需要使用其对应的标签。

在文本的实验部分，我们通过下载这些数据集并对其进行预处理，将彩色图片处理为黑白图片并进行一一对应，从而用于训练模型，使模型在花卉图上色和日常物品上色上具备更优的表现。以下为数据集示例：

![数据集展示](res/%E6%95%B0%E6%8D%AE%E9%9B%86%E5%B1%95%E7%A4%BA.png)


#### 4.2 Implementation Details

Explain how you implement your model, for example, the hyper-parameters used, the deep learning framework utilized, etc.

后端：

在原有代码基础上，通过Flask构建了一个轻量化的后端API，主要包含三个API，分别是colorize API（POST）、get_old_image API（GET）、get_color_image API（GET）。其中colorize API允许前端通过POST请求向后端上传图片，后端接受到图片后将其储存到指定路径，然后调用模型对图片进行色彩复原，生成新的图片后将其路径返回给前端。get_old_image API 要求前端提供图像名作为参数，从指定上传路径下查找对应图像，然后读取图像二进制内容返回到前端。get_color_image API要求前端提供从colorize 接口中获取的新图像路径作为参数，在指定路径中找到对应图像，然后读取图像二进制内容返回到前端。


#### 4.3 Metrics

Briefly introduce the metrics you would use to assess your model's performance in the experiments.


#### 4.4 Experimental Design & Results

Model Construction
In this work, two models are established: the generator and the critic.

Generator Model
The generator model employs a U-Net architecture, which consists of two main parts:
1. The first part performs visual recognition.
2. The second part outputs an image based on the content recognized by the first part.
   
Specifically, the first part utilizes a pre-trained ResNet34 as the backbone within the U-Net architecture to identify objects in the image. The identified backbone features are then passed to the second part, which determines the color for each part of the image, ultimately producing a colored image as the output. The goal of the generator is to establish a mapping between grayscale images and colored images.

Critic Model
The critic model is a simple convolutional network based on DG-GAN. It removes batch normalization (batchnorm) and replaces the linear output layer with a convolutional layer. This model evaluates the input images and scores the appropriateness of their colors.

Key Techniques
The most crucial aspects of both models are derived from the Self-Attention GAN paper. An "attention" layer from the Self-Attention GAN is added to both models. Additionally, spectral normalization is applied to both models. The adversarial interaction between the critic and the generator is managed using the hinge loss and different learning rates as described in the Two Time-Scale Update Rule, resulting in a more stable training process. Furthermore, the attention layer significantly enhances color continuity and overall image quality.

Training Process
The training process begins with images of 64x64 resolution and gradually increases to 96x96, 128x128, 196x196, and finally 256x256. Training with images of a uniform size can lead to poor results, such as incorrect colors and overall low-quality images. However, the improvement in the model is not due to the incremental addition of larger image sizes, but rather the gradual adjustment of the learning rate during training to accommodate larger input images. This adjustment enables the model to handle larger images more efficiently.

Model Variants
Three different models are trained in this project: Artistic, Stable, and Video.
● Artistic Model: This model tends to produce more vibrant and bold colorizations, making it suitable for artistic styles.
● Stable Model: This model produces more realistic and stable colorizations, ideal for landscapes and portraits.
● Video Model: This model addresses the flickering issue in video colorization, making it suitable for video content.

Application :grayscale images in the /gray folder can be read and colorized using different models to produce various types of colorized images. A frontend web interface is used to automatically store the output results in the /result_images folder, with the same names as the original images.


## 5. Conclusion

(What challenge you tackle with what method? How well your method is? )



## Reference
[1] jantic. DeOldify[EB/OL]. (2024-06-03). [2024-06-06]. https://github.com/jantic/DeOldify

[2] Alexander. Flowers Recognition[EB/OL]. (2021). [2024-06-06]. https://www.kaggle.com/datasets/alxmamaev/flowers-recognition

[3] FDUhangxu. flower[EB/OL]. (2024-03-19). [2024-06-06]. https://www.modelscope.cn/datasets/FDUhangxu/flower/files

[4] tany0699. dailytags[EB/OL]. (2022-12-02). [2024-06-06]. https://www.modelscope.cn/datasets/tany0699/dailytags/files



## Contributions

-   Chen Sunbing (12011118): 25%

-   Chen Tianle (12012304): 25%

-   Nian Ziyao (SID3): 25%

-   Wu Jixuan (12012301): 25%

    
