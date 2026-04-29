import streamlit as st
import plotly.express as px
from analysis import load_and_prepare_data

# Load data
df = load_and_prepare_data()

# Title
st.title("🌍 Global Health Dashboard")

# Sidebar filter
country = st.sidebar.selectbox("Select Country", df["Country"].unique())

# Filter data
filtered_df = df[df["Country"] == country]

# Show latest data (KPI)
latest = filtered_df.sort_values("Year").iloc[-1]

st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Life Expectancy", round(latest["Life Expectancy"], 2))
col2.metric("Health Expenditure", round(latest["Health Expenditure"], 2))
col3.metric("Infant Mortality", round(latest["Infant Mortality"], 2))

# Trend chart
st.subheader("📈 Life Expectancy Trend")

fig = px.line(filtered_df, x="Year", y="Life Expectancy")
st.plotly_chart(fig)