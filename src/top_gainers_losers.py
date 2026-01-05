import pandas as pd
from pathlib import Path

INPUT_FILE = Path("output/yearly_returns.csv")
OUTPUT_FOLDER = Path("output")

df = pd.read_csv(INPUT_FILE)

# Sort by return
df_sorted = df.sort_values(by="yearly_return_%", ascending=False)

# Top 5 gainers
top_gainers = df_sorted.head(5)

# Top 5 losers
top_losers = df_sorted.tail(5)

# Save outputs
top_gainers.to_csv(OUTPUT_FOLDER / "top_5_gainers.csv", index=False)
top_losers.to_csv(OUTPUT_FOLDER / "top_5_losers.csv", index=False)

print("Top gainers and losers generated successfully")
