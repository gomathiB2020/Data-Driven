import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title="Nifty 50 Stock Analysis", layout="wide")

st.title("Nifty 50 Stock Performance Dashboard")

# Load data
all_data = pd.read_csv("output/nifty50_all_data.csv")
yearly_returns = pd.read_csv("output/yearly_returns.csv")
top_gainers = pd.read_csv("output/top_5_gainers.csv")
top_losers = pd.read_csv("output/top_5_losers.csv")

# Sidebar
st.sidebar.header("Navigation")
option = st.sidebar.selectbox(
    "Select View",
    ["Raw Stock Data", "Yearly Returns", "Top Gainers", "Top Losers"]
)

# Display sections
if option == "Raw Stock Data":
    st.subheader("All Stock Data")
    st.dataframe(all_data)

elif option == "Yearly Returns":
    st.subheader("Yearly Returns of Stocks")
    st.dataframe(yearly_returns)

    # Bar chart
# Show column names (for debugging – optional)
st.write("Columns:", yearly_returns.columns.tolist())

# Automatically pick columns
x_col = yearly_returns.columns[0]   # Stock / Symbol
y_col = yearly_returns.columns[-1]  # Return column

fig, ax = plt.subplots()
ax.bar(yearly_returns[x_col], yearly_returns[y_col])
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
plt.xticks(rotation=90)

st.pyplot(fig)

