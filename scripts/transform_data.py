import pandas as pd
import os

df = pd.read_csv("../data/raw_products.csv")
df['title'] = df['title'].str.strip()
df['price'] = df['price'].astype(float)

df.to_csv("../data/clean_products.csv", index=False)
if (os.path.exists("../data/clean_products.csv")):
	print(f"Clean up and save to csv !")
else:
	print("Cleaned up file is not created")