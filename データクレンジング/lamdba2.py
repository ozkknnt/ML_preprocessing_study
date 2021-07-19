# 代入する引数x, y, z
x = 5
y = 6
z = 2

# defを用いてfunc3を作成して下さい
def func3(x,y,z):
    return x*y +z


# lambdaを用いてfunc4を作成して下さい
func4 = lambda x,y,z:x*y +z

# 出力
print(func3(x, y, z))
print(func4(x, y, z))