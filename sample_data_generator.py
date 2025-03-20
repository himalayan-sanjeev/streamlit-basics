import pandas as pd
import numpy as np
import os

# Define the output file path inside the 'data' folder
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "sample_data.csv")

# Ensure the 'data' directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate a sample dataset with multiple columns
np.random.seed(42)

num_rows = 100
df = pd.DataFrame({
    "Date": pd.date_range(start="2023-01-01", periods=num_rows, freq="D"),
    "Category": np.random.choice(["A", "B", "C", "D"], num_rows),
    "Subcategory": np.random.choice(["X", "Y", "Z"], num_rows),
    "Sales": np.random.randint(100, 1000, num_rows),
    "Profit": np.random.uniform(10, 200, num_rows),
    "Quantity": np.random.randint(1, 10, num_rows),
    "Customer_Satisfaction": np.random.randint(1, 5, num_rows),
    "Discount": np.random.uniform(0.0, 0.5, num_rows)
})

# Save to CSV
df.to_csv(OUTPUT_FILE, index=False)

print(f"CSV file saved successfully at: {OUTPUT_FILE}")
