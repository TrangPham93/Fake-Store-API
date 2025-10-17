import requests
import pandas as pd
import os

URL = "https://fakestoreapi.com/products"
data = requests.get(URL).json()

df = pd.DataFrame(data)
os.makedirs("../data", exist_ok=True)
df.to_csv("../data/raw_products.csv", index= False)

raw_product_file_path = "../data/raw_products.csv"
if os.path.exists(raw_product_file_path):
	print(f"Data fetched and saved to {raw_product_file_path}")
else:
	print(f"{raw_product_file_path} is not created")