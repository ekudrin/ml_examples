import pickle
import pandas as pd
from flask import Flask
from flask import request
from loguru import logger

app = Flask(__name__)

# загрузить модель
def load_model():
    with open('rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    return rf_model


# загрузить признаки
def load_features():
    features = pd.read_csv('pred_features.csv')
    return features

logger.info("Loading model")
model = load_model()

logger.info("Loading features")
predict_features = load_features()


# в эндпоинте добавить передачу json
@app.route('/survival', methods=['POST'])
def survival():
    json_data = request.json
    df = pd.DataFrame(json_data, index=[0])
    prediction = model.predict_proba(df.values)[:,1]

    return {
        "probability": f'Your survival probability is {prediction * 100} % '
    }