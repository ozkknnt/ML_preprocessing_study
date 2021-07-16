import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.random.chisquare(3, 20000)

y, lambda_value = stats.boxcox(x)

plt.show()