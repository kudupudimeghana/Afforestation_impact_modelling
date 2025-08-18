import streamlit as st
import pandas as pd

# --- Simulation logic ---
def run_simulation(trees, years, survival, species):
    co2_rate = {"generic": 22, "teak": 25, "mango": 18, "oak": 20}
    annual_rate = co2_rate.get(species, 22)

    surviving_trees = trees
    yearly_data = []
    total = 0

    for year in range(1, years + 1):
        surviving_trees *= survival
        co2 = surviving_trees * annual_rate
        total += co2
        yearly_data.append({"Year": year, "Surviving Trees": int(surviving_trees), "CO₂ (kg)": round(co2, 2), "Cumulative CO₂ (kg)": round(total, 2)})

    return pd.DataFrame(yearly_data)

# --- Streamlit UI ---
st.title("🌱 Afforestation Impact Modeling")
st.write("Simulate how trees capture CO₂ over years!")

# Input form
trees = st.number_input("Number of trees 🌳", min_value=1, value=10)
years = st.number_input("Years to simulate 📅", min_value=1, value=50)
survival = st.slider("Annual survival rate (%)", 0, 100, 80) / 100
species = st.selectbox("Choose tree species 🌲", ["generic", "teak", "mango", "oak"])

if st.button("Run Simulation 🚀"):
    results = run_simulation(trees, years, survival, species)

    st.subheader("📊 Yearly Data")
    st.dataframe(results)

    st.subheader("📈 CO₂ Sequestration Over Time")
    st.line_chart(results.set_index("Year")["Cumulative CO₂ (kg)"])

    st.success(f"Total CO₂ captured after {years} years: {results['Cumulative CO₂ (kg)'].iloc[-1]:,.2f} kg 🌍")
