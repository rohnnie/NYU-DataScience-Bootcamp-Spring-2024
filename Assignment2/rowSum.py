import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
row_filter = df.loc[np.where(df.sum(axis=1)>100)]
print(row_filter)
