# ==========================================
# PHASE 1: THE RAW SOURCING & INITIAL AUDIT
# ==========================================
import pandas as pd
# Step 1: Read our local financial ledger directly from our folder
df_finance = pd.read_csv('tata_stock_data.csv')

# Profile the structural footprint of our new financial ledger
print("----Step1: Financial Data Profile----")
print(df_finance.shape)
print("\n----Before: Raw Data Profile----")
print(df_finance.info())
print("\n---Before: Raw Order----")
print(df_finance.head())

# ==========================================
# PHASE 2: THE DATA ENGINEERING FIXES
# ==========================================
# 1. Convert the Date text column into actual timeline data objects
df_finance['Date'] = pd.to_datetime(df_finance['Date'])
# 2. Force the entire spreadsheet to flip chronologically from oldest date to newest date
df_finance = df_finance.sort_values(by=['Date'], ascending=True)

# ==========================================
# PHASE 3: THE POST-CLEANING VERIFICATION
# ==========================================
print("\n============================================")
print("--- AFTER: Cleaned Timeline Profile ---")
print(df_finance.info())
print("\n--- AFTER: Chronological Row Order ---")
print(df_finance.head())


# ==========================================
# PHASE 4: FINANCIAL PERFORMANCE METRICS
# ==========================================

# Question 1: Find the absolute highest peak and lowest drop in stock history
highest_peak = df_finance['High'].max()
lowest_peak = df_finance['Low'].min()

# Question 2: Find the average volume of shares traded daily
average_volume = df_finance['Total Trade Quantity'].mean()

print("\n-------Executive Metrics Summary-------")
print(f"The Absolute Market Peak: {highest_peak}")
print(f"The Absolute Market Drop: {lowest_peak}")
print(f"The Average Daily Share Volume: {average_volume:,.2f}")

# Question 3: Calculate the intra-day price spread variations
df_finance['Price_Spread'] = df_finance['High'] - df_finance['Low']
print("\n------AFTER: New Financial Column Check--------")
print(df_finance[['Date', 'High', 'Low', 'Price_Spread']].head())

# Question 4: Visualizing the Closing Price Over Time
import matplotlib.pyplot as plt
# 1. Roll out a professional 10x5 inch financial drawing canvas
plt.figure(figsize = (10, 5))
plt.plot(df_finance['Date'], df_finance['Close'], color='forestgreen', marker='o', linewidth=2)

# 3. Add clean corporate titles and labels
plt.title('Tata Global Stock: Closing Price Trend Over Time', fontsize = 14, fontweight = 'bold')
plt.xlabel('Trading Date Calendar', fontsize = 12)
plt.ylabel('Closing Share Price ($)', fontsize = 12)

# 4. Force Python to display every individual trading date and tilt them by 45 degrees
plt.xticks(df_finance['Date'], rotation=45)

# 5. Add a transparent dashed background grid line for technical eye-tracing
plt.grid(axis='both', linestyle='--', linewidth=0.5)

# 6. Apply safety borders to prevent text clipping
plt.tight_layout()

# 7. Save the chart as a high-resolution presentation image
plt.savefig('Tata_Stock_Closing_Trend.png', dpi=300)

# 8. Master launch trigger to display the chart window
plt.show(block=True)