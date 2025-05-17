from data_loader import load_and_preprocess
from model import build_model
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess('logistics_emission_data.csv')
model = build_model(X_train.shape[1])

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

y_pred = model.predict(X_test).flatten()
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
percent_error = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}, % Error: {percent_error:.2f}%")