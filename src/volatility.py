import pandas as pd

df = pd.read_csv("output/nifty50_all_data.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort
df = df.sort_values(['symbol', 'date'])

# Daily return
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# Cumulative return
df['cumulative_return'] = (1 + df['daily_return']).groupby(df['symbol']).cumprod()

# Save
df.to_csv("output/cumulative_returns.csv", index=False)

print("Done")
