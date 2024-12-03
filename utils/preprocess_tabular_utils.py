import numpy as np

def preprocess_tabular(data, scaler=None):
    """Preprocess tabular data for input into models."""
    data = np.array(data).reshape(1, -1)
    if scaler:
        data = scaler.transform(data)
    return data