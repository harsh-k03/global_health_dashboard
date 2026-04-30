import streamlit as st
import plotly.express as px
from analysis import load_and_prepare_data
from model import cluster_countries

@st.cache_data
def get_clustered_data(df):
    return cluster_countries(df)

# Page config
st.set_page_config(
    page_title="Global Health Dashboard",
    page_icon="🌍",
    layout="wide"
)

# Load data
@st.cache_data
def get_data():
    return load_and_prepare_data()

df = get_data()

# Sidebar (DEFINE BEFORE USING)
st.sidebar.title("🌍 Global Health Dashboard")
st.sidebar.markdown("Analyze global health trends")

country = st.sidebar.selectbox(
    "Select Country",
    sorted(df["Country"].unique())
)

# Title
st.title("🌍 Global Health Dashboard")

st.markdown("""
This dashboard provides insights into global health trends, comparing countries
based on life expectancy, healthcare spending, and mortality rates.
""")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Overview", "🌎 Comparison", "🤖 Insights"])

# Tab 1
with tab1:
    st.header("📊 Country Overview")

    filtered_df = df[df["Country"] == country]

    if not filtered_df.empty:
        latest = filtered_df.sort_values("Year").iloc[-1]

        col1, col2, col3 = st.columns(3)

        col1.metric("Life Expectancy", round(latest["Life Expectancy"], 2))
        col2.metric("Health Expenditure", round(latest["Health Expenditure"], 2))
        col3.metric("Infant Mortality", round(latest["Infant Mortality"], 2))

        fig = px.line(filtered_df, x="Year", y="Life Expectancy")
        st.plotly_chart(fig, use_container_width=True)

# Tab 2
with tab2:
    st.header("🌎 Global Comparison")

    latest_year = df["Year"].max()
    compare_df = df[df["Year"] == latest_year]

    top_n = st.slider("Select number of countries", 5, 30, 10)

    compare_df = compare_df.sort_values("Life Expectancy", ascending=False).head(top_n)

    fig2 = px.bar(compare_df, x="Country", y="Life Expectancy")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🌍 Global Health Map")
    
    map_df = df[df["Year"] >= 2000]
    
    fig_map = px.choropleth(
        map_df,
        locations="Code",
        color="Life Expectancy",
        hover_name="Country",
        animation_frame="Year",
        height=600
    )

    st.plotly_chart(fig_map, use_container_width=True)

# Tab 3
with tab3:
    st.header("🤖 AI Insights")

    df_clustered = get_clustered_data(df)

    fig3 = px.scatter(
        df_clustered,
        x="Health Expenditure",
        y="Life Expectancy",
        color="Cluster",
        hover_name="Country"
    )

    st.plotly_chart(fig3, use_container_width=True)