import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/clean_products.csv")
category_price = df.groupby('category')['price'].mean()

category_price.plot(kind='bar',title='Average Price per Category')
plt.ylabel('average price')
plt.tight_layout()
plt.savefig("../data/avg_price_per_category.png")
plt.show()