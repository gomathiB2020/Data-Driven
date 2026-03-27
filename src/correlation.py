import pandas as pd

df = pd.read_csv("output/nifty50_all_data.csv")

df.columns = df.columns.str.strip().str.lower()

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['symbol', 'date'])

df['daily_return'] = df.groupby('symbol')['close'].pct_change()

pivot_df = df.pivot(index='date', columns='symbol', values='daily_return')

correlation = pivot_df.corr()

correlation.to_csv("output/correlation_matrix.csv")

print("Done")
