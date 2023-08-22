from joblib import load
import numpy as np

Diabetes_prediction_model = load(filename="prediction_model.joblib")


def predict(data):
    data_size = len(data)
    data_array = np.array(data)
    sample = data_array.reshape(1, data_size)

    result = Diabetes_prediction_model.predict(sample)

    return result[0]
