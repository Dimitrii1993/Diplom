from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import json

# загружаем модель из файла
with open('Garch.pkl', 'wb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg


@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	cols = ['DATE', 'CLOSE']
	features = pd.DataFrame([features], columns=cols)
	predict = model.predict(features)
	return jsonify({'prediction': round(np.exp(predict[0]))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)