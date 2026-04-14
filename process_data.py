import pandas as pd
import glob

# Get all CSV files from data folder
files = glob.glob("data/*.csv")

# Combine all CSVs into one DataFrame
df = pd.concat([pd.read_csv(file) for file in files])

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save output
df.to_csv("output.csv", index=False)

print("Done! output.csv created.")