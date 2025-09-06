import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.set_page_config(page_title="Real-Time Data Dashboard", layout="wide")

st.title("📊 Real-Time Data Dashboard")

# Simulate real-time data stream
data = pd.DataFrame(columns=["timestamp", "value"])

placeholder = st.empty()

for i in range(100):  # generates 100 updates
    new_row = {"timestamp": pd.Timestamp.now(), "value": np.random.randint(50, 150)}
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    
    fig = px.line(data, x="timestamp", y="value", title="Live Value Stream")
    
    with placeholder.container():
        st.write("### 📈 Data Stream")
        st.dataframe(data.tail(10))  # show last 10 rows
        st.plotly_chart(fig, use_container_width=True)
    
    time.sleep(1)  # update every second
