import pandas as pd
from Tools.scripts.dutree import display

df = pd.DataFrame({"A": [1, 4, 7], "B": [2, 5, 8], "C": [3, 6, 9]})

display(df.iloc[1])
display(df.loc[1])
display(df.ix[1])

display(df.loc[:, 'A'])
display(df['A'])

# 특정 row, column을 선택하기
display(df.ix[0]['A'])
display(df.loc[0]['C'])
