#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/6 14:13
# @Author  : sunbing chen
# @File    : data_preprocess.py
# @Software: PyCharm
# @Description:
from PIL import Image
import os


def convert_to_grayscale(input_path: str, output_path: str):
    count = 0
    """
    将图片转换为灰度图并保存
    :param input_path: 彩色图片文件夹路径
    :param output_path: 灰度图保存路径
    """
    # 确保输出目录存在
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 递归遍历目录
    for root, dirs, files in os.walk(input_path):
        for filename in files:
            # 构建完整的图片文件路径
            file_path = os.path.join(root, filename)
            # 检查是否为图片文件（这里以jpg和png为例）
            if file_path.endswith(".jpg") or file_path.endswith(".png"):
                try:
                    # 打开图片
                    with Image.open(file_path) as img:
                        # 转换为灰度图
                        grayscale_img = img.convert("L")
                        # 构建输出文件的相对路径并确保目录结构
                        relative_path = os.path.relpath(root, input_path)
                        output_subdir = os.path.join(output_path, relative_path)
                        # 确保输出的子目录存在
                        if not os.path.exists(output_subdir):
                            os.makedirs(output_subdir)
                        # 构建输出文件的完整路径
                        output_file_path = os.path.join(output_subdir, filename)
                        # 保存灰度图
                        grayscale_img.save(output_file_path)
                        count += 1
                        print(f"Converted {file_path} to grayscale.")
                except IOError as e:
                    print(f"Error converting {file_path}: {e}")
    print(f"Converted {count} images.")


if __name__ == '__main__':
    in_path = 'E:/OneDrive - 南方科技大学/code/CS308_ComputerVersion/CS308-CV-Final-Image_Colorization/dataset/modelscope_dailytags'
    out_path = 'E:/OneDrive - 南方科技大学/code/CS308_ComputerVersion/CS308-CV-Final-Image_Colorization/dataset/modelscope_dailytags_gray'
    print("Converting images to grayscale...")
    convert_to_grayscale(in_path, out_path)
    print("Done.")
