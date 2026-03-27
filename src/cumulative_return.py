import pandas as pd

print("RUNNING CUMULATIVE FILE")

# Load data
df = pd.read_csv("output/nifty50_all_data.csv")

# Normalize columns
df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns)

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort properly
df = df.sort_values(['symbol', 'date'])

# Calculate daily return
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# Calculate cumulative return
df['cumulative_return'] = (1 + df['daily_return']).groupby(df['symbol']).cumprod()

# Save output
df.to_csv("output/cumulative_returns.csv", index=False)

print("CUMULATIVE DONE ")
