import cv2
import cv2.img_hash
import numpy as np

def nothing(x):
    pass

# 打开默认摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 创建一个窗口
cv2.namedWindow('Camera')

# 创建滑动条来调整 HSV 阈值
cv2.createTrackbar('H Lower', 'Camera', 0, 179, nothing)
cv2.createTrackbar('S Lower', 'Camera', 0, 255, nothing)
cv2.createTrackbar('V Lower', 'Camera', 0, 255, nothing)
cv2.createTrackbar('H Upper', 'Camera', 179, 179, nothing)
cv2.createTrackbar('S Upper', 'Camera', 255, 255, nothing)
cv2.createTrackbar('V Upper', 'Camera', 255, 255, nothing)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    
    if not ret:
        print("无法接收帧 (stream end?). Exiting ...")
        break
    
    # 将帧从 BGR 转换为 HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 获取滑动条的当前值
    h_lower = cv2.getTrackbarPos('H Lower', 'Camera')
    s_lower = cv2.getTrackbarPos('S Lower', 'Camera')
    v_lower = cv2.getTrackbarPos('V Lower', 'Camera')
    h_upper = cv2.getTrackbarPos('H Upper', 'Camera')
    s_upper = cv2.getTrackbarPos('S Upper', 'Camera')
    v_upper = cv2.getTrackbarPos('V Upper', 'Camera')
    
    # 定义 HSV 阈值范围
    lower_hsv = np.array([h_lower, s_lower, v_lower])
    upper_hsv = np.array([h_upper, s_upper, v_upper])
    
    # 应用阈值
    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # 显示原始帧和处理后的帧
    cv2.imshow('Camera', result)
    cv2.imshow('Gray', gray_frame)
    
    # 按下 'q' 键退出
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()