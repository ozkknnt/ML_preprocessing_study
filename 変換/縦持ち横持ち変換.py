import pandas as pd
import numpy as np


data = pd.DataFrame({
      '商談': np.append(np.repeat('商談1', 3), np.repeat('商談2', 3)),
      '名前': np.tile(['石川', '河合', '木村'], 2),
      '貢献度': [50, 25, 25, 60, 20, 20]
})

pivoted_data = data.pivot(index='商談', columns='名前', values='貢献度')
pivoted_data = pivoted_data.reset_index()
pivoted_data.columns = pivoted_data.columns.set_names(None)
pivoted_data