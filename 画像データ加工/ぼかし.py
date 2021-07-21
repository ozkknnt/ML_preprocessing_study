import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")

# sample.jpg をぼかしてください
my_img = cv2.GaussianBlur(img, (101, 101), 0)

cv2.imshow("sample", my_img)