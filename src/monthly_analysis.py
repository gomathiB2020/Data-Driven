import pandas as pd

print("RUNNING MONTHLY ANALYSIS ")

# Load data
df = pd.read_csv("output/nifty50_all_data.csv")

# Normalize columns
df.columns = df.columns.str.strip().str.lower()

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Extract month
df['month'] = df['date'].dt.to_period('M')

# Sort data
df = df.sort_values(['symbol', 'date'])

# Get first and last close per month
monthly_prices = (
    df.groupby(['symbol', 'month'])['close']
      .agg(['first', 'last'])
      .reset_index()
)

# Calculate monthly return
monthly_prices['monthly_return'] = (
    (monthly_prices['last'] - monthly_prices['first']) 
    / monthly_prices['first']
)

# Top 5 gainers per month
top_gainers = (
    monthly_prices.sort_values(['month', 'monthly_return'], ascending=[True, False])
    .groupby('month')
    .head(5)
)

# Top 5 losers per month
top_losers = (
    monthly_prices.sort_values(['month', 'monthly_return'])
    .groupby('month')
    .head(5)
)

# Save outputs
top_gainers.to_csv("output/monthly_gainers.csv", index=False)
top_losers.to_csv("output/monthly_losers.csv", index=False)

print("Monthly Analysis Done ✅")
print(monthly_prices.head())
