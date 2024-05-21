import joblib

def load_model():
    model = joblib.load('house_price_model.pkl')
    return model
