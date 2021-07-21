import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")
print(img.shape)

# 幅、高さをそれぞれ1/3にリサイズします
my_img = cv2.resize(img,(img.shape[1] // 3, img.shape[0] // 3))

# 出力
cv2.imshow("sample", my_img)
print(my_img.shape)