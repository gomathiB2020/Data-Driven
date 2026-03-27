import pandas as pd

# Load combined stock data
df = pd.read_csv("output/combined_stock_data.csv")

# Ensure date is datetime
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["Ticker", "date"])

# Calculate yearly return per stock
yearly_returns = (
    df.groupby("Ticker")
    .apply(lambda x: (x.iloc[-1]["close"] - x.iloc[0]["close"]) / x.iloc[0]["close"])
    .reset_index(name="yearly_return")
)

# Green and Red stocks
green_stocks = yearly_returns[yearly_returns["yearly_return"] > 0].shape[0]
red_stocks = yearly_returns[yearly_returns["yearly_return"] < 0].shape[0]

# Average price and volume
average_price = df["close"].mean()
average_volume = df["volume"].mean()

# Print summary
print("Market Summary")
print("-------------------------")
print(f"Green Stocks: {green_stocks}")
print(f"Red Stocks: {red_stocks}")
print(f"Average Price: {average_price:.2f}")
print(f"Average Volume: {average_volume:.2f}")
