# 代入する引数a
a = 4

# defを用いてfunc1を作成して下さい
def func1(a):
    return 2*a**2 - 3*a + 1

# lambdaを用いてfunc2を作成して下さい
func2 = lambda a:2*a**2 - 3*a + 1

# 返り値の出力
print(func1(a))
print(func2(a))