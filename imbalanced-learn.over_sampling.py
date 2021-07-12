# オーバーサンプリング

import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

np.random.seed(0)

data = pd.read_csv('./8000_data_preprocessing_data/imbalanced_ex.csv')
y = data['purchased']
X = data.loc[:, ['income', 'age', 'num_of_children']]

ros = RandomOverSampler(ratio = 'minority')
X_resampled, y_resampled = ros.fit_sample(X,y)
