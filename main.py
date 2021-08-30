import pandas as pd
import numpy as np

chunksize = 10000
i = 0
df = pd.read_excel("D:/python_excel/test.xlsx")
for chunk in np.array_split(df, len(df) // chunksize):
    chunk.to_excel('./excel/merck_{:02d}.xlsx'.format(i), index=True)
    i += 1