import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg", 0)

# 閾値100、それ以下を0、それ以上を255にして二値化してください
# 同時に閾値も取得してください
retval, my_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# 出力
cv2.imshow("sample", my_img)
print(retval)

