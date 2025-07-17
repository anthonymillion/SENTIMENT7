import streamlit as st
import pandas as pd
import datetime

# Asset groups
assets = {
    "Stock": ["NVDA", "MSFT", "AAPL", "AMZN", "GOOGL", "GOOG", "META", "TSLA", "AVGO", "COST", "AMD", "NFLX"],
    "Index": ["SP500", "QQQ", "USTECH100", "RUSSELL", "NIKKEI"],
    "Commodity": ["GOLD", "USOIL", "BRENT", "COPPER", "SILVER", "NATGAS"],
    "Currency": ["USDJPY", "EURUSD", "DXY", "BTCUSD"],
    "Volatility": ["VIX", "BONDYIELDS"]
}

# Timeframes
timeframes = ["1s", "5s", "15s", "30s", "M1", "M2", "M3", "M4", "M10", "M15", "M30", "H6", "H7", "H8", "1H", "4H", "Daily", "Weekly", "Monthly"]

# App settings
st.set_page_config(page_title="AI EdgeFinder – Unified Table", layout="wide")
st.title("📊 AI EdgeFinder – Unified Table View")

# Timeframe selector
selected_tf = st.selectbox("Select Timeframe", timeframes, index=timeframes.index("M15"))

# Scoring logic
def simulate_score(symbol, tf):
    base = (hash(symbol + tf + str(datetime.date.today())) % 9) - 4
    return round(base + (hash(tf) % 3 - 1), 2)

def classify_sentiment(score):
    if score > 1.5:
        return "🟢 Bullish"
    elif score < -1.5:
        return "🔴 Bearish"
    return "🟡 Neutral"

# Generate full unified table
rows = []
for category, symbols in assets.items():
    for sym in symbols:
        score = simulate_score(sym, selected_tf)
        sentiment = classify_sentiment(score)
        rows.append({
            "Category": category,
            "Symbol": sym,
            "Score": score,
            "Sentiment": sentiment
        })

df = pd.DataFrame(rows)

# Display table
st.dataframe(df.sort_values(by=["Category", "Symbol"]).reset_index(drop=True), use_container_width=True)
