import pandas as pd
# csvを読み込んでください。
df = pd.read_csv("./4050_data_cleansing_data/iris.csv",header=None)
# カラムを左の列から順に"sepal length", "sepal width", "petal length", "petal width", "class"と指定します。
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "class"] 
# DataFrameを出力してください。
df
