import pandas as pd
import requests#allows python to download filw from web browser

# URL of the CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

# Download the file content
response = requests.get(url)

# Save to local file
with open("Product-sales.csv", "wb") as f:
    f.write(response.content)

# Read it using pandas
df = pd.read_csv("Product-sales.csv")

# Display first 5 rows
print(df.head())
