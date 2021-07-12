# IsolationForest
#

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

np.random.seed(0)
data = pd.read_csv('./8000_data_preprocessing_data/outlier_ex.csv')

clf = IsolationForest()
clf.fit(data)
predictions = clf.predict(data)
data[predictions == -1]
