import pandas as pd

print("RUNNING SECTOR ANALYSIS FINAL ✅")

# Load data
df = pd.read_csv("output/nifty50_all_data.csv")
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# Normalize columns
df.columns = df.columns.str.strip().str.lower()
sector_df.columns = sector_df.columns.str.strip().str.lower()

# Clean values
df['symbol'] = df['symbol'].astype(str).str.strip().str.upper()
sector_df['company'] = sector_df['company'].astype(str).str.strip().str.upper()

print("Main symbols sample:", df['symbol'].unique()[:5])
print("Company sample:", sector_df['company'].unique()[:5])

# 🔥 Create mapping using COMPANY
sector_map = dict(zip(sector_df['company'], sector_df['sector']))

# Map using symbol → company assumption
df['sector'] = df['symbol'].map(sector_map)

# Debug
print("Missing sectors:", df['sector'].isna().sum())

# Convert date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['symbol', 'date'])

# Daily return
df['daily_return'] = df.groupby('symbol')['close'].pct_change()

# Drop NaN
df = df.dropna(subset=['daily_return', 'sector'])

# Sector performance
sector_perf = df.groupby('sector')['daily_return'].mean().reset_index()
sector_perf.columns = ['sector', 'average_return']

# Save
sector_perf.to_csv("output/sector_performance.csv", index=False)

print("Sector Done ✅")
print(sector_perf)
