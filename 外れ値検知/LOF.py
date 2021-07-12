# scikit-learnを使って
# LOFを実装する。

import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

np.random.seed(0)
data = pd.read_csv('./8000_data_preprocessing_data/outlier_ex.csv')


clf = LocalOutlierFactor(n_neighbors=20)
predictions = clf.fit_predicit(data)
