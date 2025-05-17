import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Title
st.title("Carbon Footprint Optimizer - Supply Chain Logistics")

# Upload Dataset
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data.head())

    # Check if required columns exist
    required_features = ['route_distance', 'fuel_usage', 'weather_index', 'traffic_level', 'cargo_weight']
    target = 'carbon_emission'

    if all(feature in data.columns for feature in required_features) and target in data.columns:
        # Handle missing values by filling mean
        data.fillna(data.select_dtypes(include=np.number).mean(), inplace=True)

        # Prepare features and target
        X = data[required_features]
        y = data[target]

        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        percent_error = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

        st.write(f"**MAE:** {mae:.4f}")
        st.write(f"**RMSE:** {rmse:.4f}")
        st.write(f"**Percent Error:** {percent_error:.2f}%")

        # Plot actual vs predicted
        fig, ax = plt.subplots()
        ax.scatter(y_test, y_pred, alpha=0.7)
        ax.set_xlabel("Actual Carbon Emission")
        ax.set_ylabel("Predicted Carbon Emission")
        ax.set_title("Actual vs Predicted Carbon Emission")
        st.pyplot(fig)

    else:
        st.error(f"Dataset must include columns: {required_features + [target]}")

else:
    st.info("Please upload a CSV file to proceed.")
