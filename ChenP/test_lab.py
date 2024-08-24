import cv2
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

# 创建滑动条来调整 LAB 阈值
cv2.createTrackbar('L Lower', 'Camera', 0, 255, nothing)
cv2.createTrackbar('A Lower', 'Camera', 0, 255, nothing)
cv2.createTrackbar('B Lower', 'Camera', 0, 255, nothing)
cv2.createTrackbar('L Upper', 'Camera', 255, 255, nothing)
cv2.createTrackbar('A Upper', 'Camera', 255, 255, nothing)
cv2.createTrackbar('B Upper', 'Camera', 255, 255, nothing)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    
    if not ret:
        print("无法接收帧 (stream end?). Exiting ...")
        break
    
    # 将帧从 BGR 转换为 LAB
    lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    
    # 获取滑动条的当前值
    l_lower = cv2.getTrackbarPos('L Lower', 'Camera')
    a_lower = cv2.getTrackbarPos('A Lower', 'Camera')
    b_lower = cv2.getTrackbarPos('B Lower', 'Camera')
    l_upper = cv2.getTrackbarPos('L Upper', 'Camera')
    a_upper = cv2.getTrackbarPos('A Upper', 'Camera')
    b_upper = cv2.getTrackbarPos('B Upper', 'Camera')
    
    # 定义 LAB 阈值范围
    lower_lab = np.array([l_lower, a_lower, b_lower])
    upper_lab = np.array([l_upper, a_upper, b_upper])
    
    # 应用阈值
    mask = cv2.inRange(lab_frame, lower_lab, upper_lab)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # 显示原始帧和处理后的帧
    cv2.imshow('Camera', result)
    
    # 按下 'q' 键退出
    if cv2.waitKey(1) == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()