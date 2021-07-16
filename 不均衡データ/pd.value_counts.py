import pandas as pd

data = pd.read_csv('./8000_data_preprocessing_data/imbalanced_ex.csv')

data['purchased'].value_counts()

# 各値の頻度を知ることができる