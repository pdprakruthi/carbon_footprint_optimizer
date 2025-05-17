import pandas as pd

def suggest_best_route(route_options, model, preprocessor):
    emissions = []
    for route in route_options:
        df = pd.DataFrame([route])
        X = preprocessor.transform(df)
        predicted_emission = model.predict(X)[0][0]
        emissions.append((route, predicted_emission))

    emissions.sort(key=lambda x: x[1])
    return emissions[0]