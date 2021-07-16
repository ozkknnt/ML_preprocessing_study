# オーバーサンプリングとアンダーサンプリングを両方使う
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import EditedNearestNeighbours
from imblearn.combine import SMOTEENN

np.random.seed(0)

data = pd.read_csv('./8000_data_preprocessing_data/imbalanced_ex.csv')
y = data['purchased']
X = data.loc[:, ['income', 'age', 'num_of_children']]

sm_enn = SMOTEENN(smote=SMOTE(k_neighbors=3),enn=EditedNearestNeighbours(n_neighbors=3))
X_resampled, y_resampled = sm_enn.fit_sample(X,y) 
(X_resampled, y_resampled)