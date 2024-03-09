import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv',storage_options={'verify': False})
df_filter=df.iloc[::20].filter(items=['Manufacturer','Model','Type'])
print(df_filter.head())

