import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
from statsforecast import StatsForecast
from statsforecast.models import Theta

# === Page Config ===
st.set_page_config(page_title="Pearl Brands", layout="wide")

# === Inject Custom CSS ===
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
        }
        h1, h2, h3, h4 {
            color: #2c2c54;
        }
        .big-title {
            font-size: 48px;
            color: #4B0082;
            text-align: center;
            font-weight: bold;
        }
        .gold-line {
            border: none;
            height: 2px;
            background-color: #bfa046;
            margin: 30px 0;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar Navigation ===
page = st.sidebar.radio(
    " ",
    ["Home", "KPI Dashboard", "Forecast Dashboard", "Theta Model Forecast"]
)

# === HOME PAGE ===
if page == "Home":
    st.image("PB banner.png", use_column_width=True)
    st.markdown('<div class="big-title">Pearl Brands</div>', unsafe_allow_html=True)
    st.markdown('<hr class="gold-line"/>', unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    <b>Pearl Brands SAL</b> is Lebanon’s gateway to premium retail, curating global fashion and beauty icons under one resilient, visionary umbrella.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Key Highlights")
    st.markdown("""
    - Exclusive partnerships with elite global brands  
    - Presence in Beirut Souks, ABC, downtown hubs  
    - Diverse portfolio: apparel, beauty, lifestyle  
    - Proven resilience through crisis and recovery  
    """)

    st.markdown("### Vision & Mission")
    st.markdown("""
    - Deliver an elevated, personalized retail journey  
    - Use digital and data to lead smart growth  
    - Expand our physical and online footprint across Lebanon and beyond  
    """)

    st.markdown('<hr class="gold-line"/>', unsafe_allow_html=True)
    st.info("This digital dashboard is part of Pearl Brands’ commitment to innovation through data, strategy, and customer insight.")

# === KPI DASHBOARD ===
elif page == "KPI Dashboard":
    st.title("Pearl Brands KPI Dashboard")
    st.markdown("Explore interactive Tableau dashboards showing key metrics across brands, sales, locations, and demographics.")

    st.subheader("1 – Sales Over Time and by Period Type")
    components.iframe(
        "https://public.tableau.com/views/SalesOvertimeandbyPeriodType/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("2 – Sales by Location and Category")
    components.iframe(
        "https://public.tableau.com/views/SalesbyLocationandCategory_17448326135380/Dashboard2?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("3 – Brand Performance")
    components.iframe(
        "https://public.tableau.com/views/BrandsPerformance/Dashboard3?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("4 – Profit Margin and Sales")
    components.iframe(
        "https://public.tableau.com/views/ProfitMarginandSales_17448337825990/Dashboard4?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1500
    )

    st.subheader("5 – Quantities and Prices")
    components.iframe(
        "https://public.tableau.com/views/QuantitiesandPrices/Dashboard5?:embed=y&:display_count=yes&:showVizHome=no",
        height=1027, width=1500
    )

    st.subheader("6 – Gender and Category Profit Margin")
    components.iframe(
        "https://public.tableau.com/views/GenderandCategoryProfitMargin/Dashboard6?:embed=y&:display_count=yes&:showVizHome=no",
        height=1027, width=1500
    )

# === FORECAST DASHBOARD ===
elif page == "Forecast Dashboard":
    st.title("Pearl Brands Forecast Dashboard")
    st.image("BestModel.png", caption="Pearl Brands 2025–2030 Forecast (TBATS Model)", use_column_width=True)

    st.markdown("""
    ### Key Takeaways:

    - The **TBATS Model** was selected as the optimal forecasting solution after benchmarking against various statistical and machine learning models. It stood out by handling **multiple seasonal patterns**, **trend shifts**, and **external disruptions** better than other approaches.

    - TBATS is particularly suited for **Lebanon’s dynamic retail market**, where sales patterns are influenced by holidays, economic volatility, and regional conflict. It captures both **short-term fluctuations** and **long-term seasonal effects** with high accuracy.

    - The model supports key strategic pillars:
        - **Brand Portfolio Planning**: Forecasted category trends (e.g., beauty, kidswear, activewear) inform decisions on brand acquisition, influencer marketing, and campaign targeting.
        - **Inventory & Supply Chain Management**: Predictive insights improve seasonal stock planning, reduce excess inventory, and optimize warehousing across regions.
        - **Location Expansion Strategy**: TBATS enables data-driven decisions for growth in underserved areas like **Saida**, **Tripoli**, and **Zahle** through demand mapping.

    - TBATS forecasts are designed to evolve, forming part of an ongoing **feedback loop**:
        - Frequent updates using the most recent sales data
        - Integration of **external variables** (currency rates, conflict timelines, inflation trends)
        - Simulation of **best/worst-case scenarios** for resilience planning

    - For long-term success, Pearl Brands should maintain **forecast governance** by:
        - Monitoring deviation between predicted and actual performance
        - Fine-tuning the model based on marketing calendars, online traffic surges, or supply chain disruptions
        - Collaborating across departments to ensure forecasts guide execution

    > This forecast is not just a number — it’s Pearl Brands’ **strategic compass**, equipping the team to make proactive, data-driven decisions in a challenging and ever-shifting retail environment.
    """)


# === THETA MODEL FORECAST PAGE ===
elif page == "Theta Model Forecast":
    st.title("📈 Theta Model Forecast (Last 2 Years + 12 Months Ahead)")

    uploaded_file = st.file_uploader("Upload your Parquet file", type=["parquet"])

    if uploaded_file is not None:
        import pandas as pd
        import matplotlib.pyplot as plt
        from statsforecast import StatsForecast
        from statsforecast.models import Theta

        # Load and clean the uploaded parquet file
        data = pd.read_parquet(uploaded_file)
        data.columns = data.columns.str.strip()

        st.success("✅ Parquet data successfully loaded!")
        st.write("🧠 Columns in your uploaded file:", data.columns.tolist())
        st.write(data.head())

        # === Auto-detect and rename 'Year-Month' column ===
        if "Year-Month" not in data.columns:
            possible_matches = [col for col in data.columns if "year" in col.lower() and "month" in col.lower()]
            if possible_matches:
                data.rename(columns={possible_matches[0]: "Year-Month"}, inplace=True)
                st.info(f"🔁 Renamed '{possible_matches[0]}' to 'Year-Month' automatically.")
            else:
                st.error("❌ Column 'Year-Month' not found and no likely match detected.")
                st.stop()

        # === Convert to datetime ===
        try:
            data["Year-Month"] = pd.to_datetime(data["Year-Month"], format="%Y-%m-%d")
        except Exception as e:
            st.error(f"❌ Failed to parse 'Year-Month': {e}")
            st.stop()

        # === Forecast logic ===
        recent_data = data[data["Year-Month"] >= data["Year-Month"].max() - pd.DateOffset(years=2)]
        monthly_sales = (
            recent_data.groupby("Year-Month")["Sale Amount in USD"]
            .sum()
            .reset_index()
            .sort_values("Year-Month")
        )

        df_theta = monthly_sales.copy()
        df_theta.columns = ['ds', 'y']
        df_theta['unique_id'] = 'total_sales'
        df_theta = df_theta[['unique_id', 'ds', 'y']]

        sf = StatsForecast(models=[Theta(season_length=12)], freq='MS', n_jobs=1)
        forecast = sf.forecast(df=df_theta, h=12)

        # === Visualization ===
        st.subheader("📊 Forecast Visualization")
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(df_theta['ds'], df_theta['y'], label='Historical Sales', color='blue')
        ax.plot(forecast['ds'], forecast['Theta'], label='Theta Forecast', color='orange')
        ax.axvline(x=df_theta['ds'].max(), color='red', linestyle='--', label='Forecast Start')
        ax.set_title("Theta Model Sales Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales Amount (USD)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

        # === Forecast Table ===
        st.subheader("📄 Forecast Table")
        st.dataframe(forecast)

        # === Download Option ===
        st.download_button(
            label="📥 Download Forecast CSV",
            data=forecast.to_csv(index=False),
            file_name="theta_forecast.csv",
            mime="text/csv"
        )

    else:
        st.warning("📂 Please upload your `.parquet` file to generate the forecast.")

