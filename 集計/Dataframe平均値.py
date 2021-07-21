import pandas as pd

df = pd.read_csv("./4050_data_cleansing_data/wine.csv", header=None)
df.columns = ["", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoids",
              "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
              
df["Magnesium"].mean()