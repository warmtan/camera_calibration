import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

import pyrealsense2 as rs

# ；案例1： 初始化工作
# 注意要预先知道彩色图像和深度图像的分辨率，否则报错。

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 30)
config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
# pipeline.start(config)

pf = pipeline.start(config) 
print(f"device: {pf.get_device()}")
print(f"depth_sensor: {pf.get_device().first_depth_sensor()}")
print(f"depth_scale: {pf.get_device().first_depth_sensor().get_depth_scale()}")
print(f"streams: {pf.get_streams()}")

# 案例2： 读取一帧数据
# 将深度图对齐到RGB
# align_to = rs.stream.color
# align = rs.align(align_to)
# print(f"align:{align}")

# 获取Realsence一帧的数据
# frame = pipeline.wait_for_frames()

# frame的基本元素
# print(f"data: {frame.data}")
# print(f"frame_number: {frame.frame_number}")
# print(f"frame_timestamp_domain: {frame.frame_timestamp_domain}")
# print(f"profile: {frame.profile}")
# print(f"timestamp: {frame.timestamp}")

