import numpy as np
from sklearn import preprocessing

np.random.seed(0)

# 平均 50、分散10の正規分布データを10個生成
data = np.random.normal(50, 10, 10)

# 平均0、分散1のデータに調整
scaled_x = preprocessing.scale(data)
