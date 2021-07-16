import pandas as pd
df = pd.DataFrame({'height': ['190台', '180台', '170台', '160台', '170台', '180台', '150台']})

pd.get_dummies(df['height'])
