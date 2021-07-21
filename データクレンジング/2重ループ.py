#二進数で３桁目を示すfours_placeと２桁目を示すtwos_place、１桁目を示すones_placeを用いて、十進数で0から7までの数を配列にして出力して下さい。
#例えばfours_place = 1, twos_place = 0, ones_place = 1であれば、
#二進数で101を意味するので、十進数では5となります。

# 二進数の桁
fours_place = [0, 1]
twos_place  = [0, 1]
ones_place  = [0, 1]

# リスト内包表記の多重ループを用いて0から7までの整数を計算し、配列にして下さい
digit = [x*4 + y*2 + z for x in fours_place for y in twos_place for z in ones_place]

# 出力して下さい
print(digit)
