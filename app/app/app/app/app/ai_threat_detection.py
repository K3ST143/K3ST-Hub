import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_threat_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def detect_threat(model, X):
    return model.predict(X)
