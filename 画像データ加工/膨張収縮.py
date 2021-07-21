import numpy as np
import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg", 0)
retval, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# フィルタを定義してください
filt = np.array([[0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]], np.uint8)

# 収縮してください
my_img = cv2.erode(img, filt)

# 表示
cv2.imshow("sample", my_img)
# 比較のため元の写真も表示
cv2.imshow("original", img)