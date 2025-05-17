import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)

    X = df.drop('emission_kg', axis=1)
    y = df['emission_kg']

    num_features = ['distance_km', 'cargo_weight_kg', 'avg_speed_kmph',
                    'traffic_level', 'wind_speed_kmph', 'rain_intensity']
    cat_features = ['fuel_type']

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(), cat_features)
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_trans = preprocessor.fit_transform(X_train)
    X_test_trans = preprocessor.transform(X_test)

    return X_train_trans, X_test_trans, y_train, y_test, preprocessor