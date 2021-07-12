# アンダーサンプリング

import numpy as np
import pandas as pd
from imblearn.under_sampling import RandomUnderSampler

np.random.seed(0)

data = pd.read_csv('./8000_data_preprocessing_data/imbalanced_ex.csv')
y = data['purchased']
X = data.loc[:, ['income', 'age', 'num_of_children']]


rus = RandomUnderSampler(ratio = 'majority')
X_resampled, y_resampled = rus.fit_sample(X,y)
