import pandas as pd
from pathlib import Path

INPUT_FILE = Path("output/nifty50_all_data.csv")
OUTPUT_FILE = Path("output/yearly_returns.csv")

df = pd.read_csv(INPUT_FILE)

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

df = df.sort_values(by=["symbol", "year", "date"])

result = []

for (symbol, year), group in df.groupby(["symbol", "year"]):
    first_close = group.iloc[0]["close"]
    last_close = group.iloc[-1]["close"]

    yearly_return = ((last_close - first_close) / first_close) * 100

    result.append({
        "symbol": symbol,
        "year": year,
        "first_close": first_close,
        "last_close": last_close,
        "yearly_return_%": round(yearly_return, 2)
    })

final_df = pd.DataFrame(result)
final_df.to_csv(OUTPUT_FILE, index=False)

print("Yearly returns saved to:", OUTPUT_FILE)
