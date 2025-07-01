import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# 🚗⚡ Electric Car Sales Dashboard
# ==========================

@st.cache_data
def load_data():
    df = pd.read_csv('EV.csv')
    return df

df = load_data()

st.set_page_config(page_title="EV Sales Analytics Dashboard", layout="wide")
st.title("🚗⚡ Electric Car Sales Analytics Dashboard")

# ==========================
# Sidebar Filters
# ==========================
st.sidebar.header("🔎 Filter Options")

regions = st.sidebar.multiselect(
    "Select Regions:",
    df['region'].unique(),
    default=df['region'].unique()
)

powertrains = st.sidebar.multiselect(
    "Select Powertrains:",
    df['powertrain'].unique(),
    default=df['powertrain'].unique()
)

years = st.sidebar.slider(
    "Select Year Range:",
    int(df['year'].min()), int(df['year'].max()),
    (int(df['year'].min()), int(df['year'].max()))
)

# Filtered data
filtered_df = df[
    (df['region'].isin(regions)) &
    (df['powertrain'].isin(powertrains)) &
    (df['year'].between(years[0], years[1]))
]

st.sidebar.markdown("---")
st.sidebar.write(f"📊 Data points: {len(filtered_df)}")

# ==========================
# Main Tabs
# ==========================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Global EV Sales",
    "📊 Regional EV Sales",
    "⚡ Electricity Demand",
    "🛢️ Oil Displacement",
    "📈 EV Stock Share"
])

# ==========================
# 1️⃣ Global EV Sales Over Years
# ==========================
with tab1:
    st.subheader("🌍 Global EV Sales Over Years")
    ev_sales = filtered_df[filtered_df['parameter'] == 'EV sales']
    if not ev_sales.empty:
        global_sales = ev_sales.groupby('year')['value'].sum().reset_index()
        fig = px.line(global_sales, x='year', y='value', markers=True,
                      title='Global EV Sales', labels={'value': 'Vehicles Sold'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No EV sales data for selected filters.")

# ==========================
# 2️⃣ Regional EV Sales Trends
# ==========================
with tab2:
    st.subheader("📊 Regional EV Sales Trends")
    ev_sales = filtered_df[filtered_df['parameter'] == 'EV sales']
    if not ev_sales.empty:
        regional_sales = ev_sales.groupby(['year', 'region'])['value'].sum().reset_index()
        fig = px.line(regional_sales, x='year', y='value', color='region', markers=True,
                      title='Regional EV Sales Trends', labels={'value': 'Vehicles Sold'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No EV sales data for selected filters.")

# ==========================
# 3️⃣ Electricity Demand Trends
# ==========================
with tab3:
    st.subheader("⚡ Electricity Demand by EVs")
    elec = filtered_df[filtered_df['parameter'] == 'Electricity demand']
    if not elec.empty:
        elec_summary = elec.groupby(['year', 'region'])['value'].sum().reset_index()
        fig = px.line(elec_summary, x='year', y='value', color='region', markers=True,
                      title='Electricity Demand by Region (GWh)', labels={'value': 'GWh'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No electricity demand data for selected filters.")

# ==========================
# 4️⃣ Oil Displacement due to EVs
# ==========================
with tab4:
    st.subheader("🛢️ Oil Displacement due to EVs")
    oil = filtered_df[filtered_df['parameter'] == 'Oil displacement Mbd']
    if not oil.empty:
        oil_summary = oil.groupby(['year', 'region'])['value'].sum().reset_index()
        fig = px.line(oil_summary, x='year', y='value', color='region', markers=True,
                      title='Oil Displacement by Region (Million barrels/day saved)',
                      labels={'value': 'Mbd'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No oil displacement data for selected filters.")

# ==========================
# 5️⃣ EV Stock Share by Region
# ==========================
with tab5:
    st.subheader("📈 EV Stock Share by Region (%)")
    stock = filtered_df[filtered_df['parameter'] == 'EV stock share']
    if not stock.empty:
        stock_summary = stock.groupby(['year', 'region'])['value'].mean().reset_index()
        fig = px.line(stock_summary, x='year', y='value', color='region', markers=True,
                      title='EV Stock Share by Region (%)', labels={'value': 'Percent Share'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No EV stock share data for selected filters.")

st.success("✅ Dashboard loaded successfully! Adjust filters to explore insights.")
