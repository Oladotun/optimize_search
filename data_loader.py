import pandas as pd

df = pd.read_csv("./HPI_master.csv")
df = df[df["yr"]== 2023]
# print(df.yr.unique())
df.to_csv("house_prices_2023.csv",index=False)