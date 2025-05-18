import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the App
st.title("Carbon Footprint Optimizer 🌍")

st.header("Calculate and Reduce Your Carbon Footprint")

# User Input for Carbon Emission Categories
st.subheader("Enter your carbon usage for different activities")

# Example Input Fields
transportation = st.number_input("Transportation (kg CO2/month)", min_value=0.0, format="%.2f")
energy_consumption = st.number_input("Home Energy Consumption (kg CO2/month)", min_value=0.0, format="%.2f")
food_consumption = st.number_input("Food Consumption (kg CO2/month)", min_value=0.0, format="%.2f")
other_activities = st.number_input("Other Activities (kg CO2/month)", min_value=0.0, format="%.2f")

# Calculate Total Carbon Footprint
total_emissions = transportation + energy_consumption + food_consumption + other_activities
st.write(f"### Your Estimated Carbon Footprint: {total_emissions:.2f} kg CO2/month")

# Suggestions for Reducing Carbon Footprint
st.subheader("Ways to Reduce Your Carbon Footprint")

if total_emissions > 500:
    st.warning("Your footprint is quite high! Consider reducing air travel, switching to renewable energy, and reducing meat consumption.")
elif total_emissions > 250:
    st.info("Your footprint is moderate. You can reduce energy waste, use public transport, and opt for plant-based foods.")
else:
    st.success("Great job! Keep maintaining a low carbon footprint by making sustainable choices.")

# Visualization
st.subheader("Carbon Footprint Breakdown")
data = {
    "Activity": ["Transportation", "Energy", "Food", "Other"],
    "Emissions": [transportation, energy_consumption, food_consumption, other_activities]
}
df = pd.DataFrame(data)
fig, ax = plt.subplots()
ax.bar(df["Activity"], df["Emissions"], color=["blue", "green", "orange", "red"])
ax.set_ylabel("kg CO2/month")
st.pyplot(fig)

st.write("### Take Action Today! 🌱")
