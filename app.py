import streamlit as st
import plotly.express as px
from analysis import load_and_prepare_data
from model import cluster_countries

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

# Country comparison
st.subheader("🌎 Country Comparison (Latest Year)")

latest_year = df["Year"].max()
compare_df = df[df["Year"] == latest_year]

top_n = st.slider("Select number of countries", 5, 30, 10)

compare_df = compare_df.sort_values("Life Expectancy", ascending=False).head(top_n)

fig2 = px.bar(
    compare_df,
    x="Country",
    y="Life Expectancy"
)

st.plotly_chart(fig2)

# World Map
st.subheader("🌍 Global Health Map")

fig_map = px.choropleth(
    df,
    locations="Code",              # Country codes (important)
    color="Life Expectancy",
    hover_name="Country",
    animation_frame="Year"
)

st.plotly_chart(fig_map)

# Apply clustering
df_clustered = cluster_countries(df)

st.subheader("🤖 Country Clusters")

fig3 = px.scatter(
    df_clustered,
    x="Health Expenditure",
    y="Life Expectancy",
    color="Cluster",
    hover_name="Country"
)

st.plotly_chart(fig3)