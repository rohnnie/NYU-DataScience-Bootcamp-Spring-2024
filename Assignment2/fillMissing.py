import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price']=df['Min.Price'].fillna(df['Min.Price'].mean())
df['Max.Price']=df['Max.Price'].fillna(df['Max.Price'].mean())

