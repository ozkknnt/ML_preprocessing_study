import cv2

img = cv2.imread("./4050_data_cleansing_data/sample.jpg")

# OpenCVで色を反転します
my_img = cv2.bitwise_not(img)

# 変換処理は内部では下記のような処理を行っている
#for i in range(len(img)):
#    for j in range(len(img[i])):
#        # RGBチャネル(k:0-2)を取得
#        for k in range(len(img[i][j])):
#            # 座標(i, j)のRGBチャネル(k:0-2)ごとに画素値を変換
#            img[i][j][k] = 255 - img[i][j][k]

            
cv2.imshow("sample", img)