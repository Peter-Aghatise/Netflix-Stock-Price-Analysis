# 📈 Historical Equity Volatility & Timeline Tracker

## 🏢 Business Overview
This data analytics project builds a dedicated financial tracking engine to ingest, clean, and profile time-series asset ledger transactions. By auditing standard **OHLC (Open-High-Low-Close)** market fingerprints, this tool extracts key performance metrics, evaluates day-trading risks, and visualizes market price trajectories for corporate investment portfolios.

---

## 🎯 Key Business Questions Answered
1. **Absolute Market Extremes:** What was the highest peak and lowest drop of the asset over the trading period?
2. **Liquidity Analysis:** What was the average daily trading volume of the stock?
3. **Risk & Volatility Evaluation:** What were the intra-day price variations and spreads across each calendar day?
4. **Chronological Trajectory:** How did the final closing price trend over time?

---

## 📊 Executive Summary & Data Insights

### 1. Key Performance Indicators (KPIs)
* **Absolute Market Peak:** $248.55
* **Absolute Market Drop:** $180.70
* **Average Daily Trading Volume:** 2,857,791.10 Shares (Indicating robust market liquidity).

### 2. Intra-Day Price Spread & Volatility Analysis
Our custom feature equation calculated the mathematical difference between the daily `High` and daily `Low`. 
* On **September 24th**, the spread exploded to its absolute peak of **10.55**, indicating high active day-trading risk and heavy speculation.
* Moving into October, the daily price spread compressed significantly, stabilizing to an average range of **5.50 to 5.90**. This proves that intra-day chaos subsided as the stock found a stable, predictable trading floor.

### 3. Closing Price Trajectory
The asset underwent a clear **Bear Trend** across the timeline. After opening at its peak on September 24th, heavy market sell-offs continuously dragged the valuation downward by over 27%, hitting a major support floor of $180.70 on October 4th before a slight correction.

---

## 🛠️ Data Engineering & Cleaning Workflow
* **Temporal Realignment:** Converted string calendar records into clean `datetime64[ns]` time objects.
* **Chronological Inversion:** Corrected a critical factory formatting error by sorting the dataset chronologically forward from oldest to newest date, protecting the visual pipeline from right-to-left timeline distortion bugs.
* **Feature Engineering:** Developed a new calculated database column (`Price_Spread`) to isolate and track intra-day volatility variations.
* **Visual Optimization:** Generated high-resolution, production-ready timeline trend visualizations utilizing `Matplotlib` exported at a razor-sharp **300 DPI**.

---

## 💻 Tech Stack & Libraries Used
* **Language:** Python 3.14
* **Data Manipulation:** Pandas
* **Mathematical Operations:** NumPy
* **Data Visualization:** Matplotlib
