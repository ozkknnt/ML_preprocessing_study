import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")
mask = cv2.imread("./4050_data_cleansing_data/mask.png", 0)
mask = cv2.resize(mask, (img.shape[1], img.shape[0]))

# mask.pngの黒い部分のみを表示します（黒の画素数は`0`です）
retval, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV)
my_img = cv2.bitwise_and(img, img, mask = mask)

# 出力
cv2.imshow("sample", my_img)