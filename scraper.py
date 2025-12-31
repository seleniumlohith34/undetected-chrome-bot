from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://example-ecom.com")
products = driver.find_elements("css selector", ".product")
df = pd.DataFrame({"name":[p.text for p in products]})
df.to_csv("products.csv")
print("Scraped successfully!")
