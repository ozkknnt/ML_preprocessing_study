import pandas as pd

data = pd.DataFrame({
    '商談': ['商談1', '商談2'],
    '木村': [25, 20],
    '河合': [25, 20],
    '石川': [50, 60]
})

pd.melt(data,id_vars=['商談'],value_vars=['木村','河合','石川'],var_name='名前',value_name='貢献度')
