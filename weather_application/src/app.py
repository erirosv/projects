import streamlit as st
import pandas as pd
from database import engine

st.set_page_config(page_title="Live Weather Dashboard", layout="wide")
st.title("Live Weather Dashboard")

df = pd.read_sql('SELECT * FROM weather ORDER BY timestamp DESC LIMIT 100', engine)
df['timestamp'] = pd.to_datetime(df['timestamp'])

st.dataframe(df)

st.line_chart(df.sort_values('timestamp')[['timestamp', 'temperature']].set_index('timestamp'))
st.line_chart(df.sort_values('timestamp')[['timestamp', 'humidity']].set_index('timestamp'))
