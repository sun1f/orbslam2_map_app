import numpy
import rosbag
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
rgb_path = '/home/sun/demo4_ws/rgb/'  # absolute path of extracted rgb images
# absolute path of extracted depth images
depth_path = '/home/sun/demo4_ws/depth/'
bridge = CvBridge()
with rosbag.Bag('/home/sun/demo4_ws/2021-12-10-19-00-15.bag', 'r') as bag:
    num = 1
    for topic,msg,t in bag.read_messages():
        
        if topic == "/camera/depth/image_rect_raw": 
            cv_image = bridge.imgmsg_to_cv2(msg, '32FC1')
            cv_image = cv_image * 255  # 不知为何转化的深度图显示不出来。将其乘以 255 才能看到显示效果.

            # timestr = "%.8f" %  msg.header.stamp.to_sec() # 时间戳命名
            # image_name = timestr + '.png'# an extension is necessary
            image_name = str(num) + '.png'# 编号命名
            cv2.imwrite(depth_path + image_name, cv_image)  
            # 实际应用可直接保存为 numpy array
            # np.save(depth_path + image_name, cv_image)  
            print(depth_path + image_name)
        if topic == "/camera/color/image_raw": 
            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
            timestr = "%.8f" %  msg.header.stamp.to_sec()
            image_name = str(num) + '.png'
            cv2.imwrite(rgb_path + image_name, cv_image)
        num += 1

