import requests
import pandas as pd
import os
import sys

URL = "https://fakestoreapi.com/products"

# try except block to request data from API
try:
	response = requests.get(URL, timeout=10)
	response.raise_for_status()
	data = response.json()
except (requests.exceptions.RequestException, ValueError) as e:
	print(f"Error: failed to fetch data [{e}]")
	sys.exit(1)

# create a folder data if not exist, and convert the data to csv form
try:
	df = pd.DataFrame(data)
	os.makedirs("../data", exist_ok=True)
	df.to_csv("../data/raw_products.csv", index= False)
except Exception as e:
	print(f"Error: failed to save csv [{e}]")
else:
# test if the file is created or not
	raw_product_file_path = "../data/raw_products.csv"
	if os.path.exists(raw_product_file_path):
		print(f"Data fetched and saved to {raw_product_file_path}")
	else:
		print(f"{raw_product_file_path} is not created")