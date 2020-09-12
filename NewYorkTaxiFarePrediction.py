import pickle
import json
import numpy as np
from xgboost import Booster, XGBRegressor

model = None

def load_saved_attributes():
    global model

    model = XGBRegressor()
    booster = Booster()
    booster.load_model('./ny_taxi_fare')
    model._Booster = booster


def predict_fare(passenger_count, month, day, hour, minute, meridiem, weekday, total_distance):
    sample = (np.array([passenger_count, month, day, hour, minute, meridiem, weekday, total_distance]))
    return model.predict(sample.reshape(1,-1))[0]


if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()
