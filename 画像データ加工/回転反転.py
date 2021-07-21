import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")

# x軸を中心に画像を反転してください
my_img = cv2.flip(img, 0)

cv2.imshow("sample", my_img)