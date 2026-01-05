import yaml
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")
OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

all_records = []

for month_folder in DATA_PATH.iterdir():
    if month_folder.is_dir():
        for yaml_file in month_folder.glob("*.yaml"):
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            for record in data:
                all_records.append({
                    "date": record.get("date"),
                    "month": record.get("month"),
                    "symbol": record.get("Ticker"),
                    "open": record.get("open"),
                    "high": record.get("high"),
                    "low": record.get("low"),
                    "close": record.get("close"),
                    "volume": record.get("volume"),
                })

df = pd.DataFrame(all_records)
df["date"] = pd.to_datetime(df["date"])

df.to_csv(OUTPUT_PATH / "nifty50_all_data.csv", index=False)

print("CSV created successfully")
print("Total rows:", len(df))
print(df.head())
