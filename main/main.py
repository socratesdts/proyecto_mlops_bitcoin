
from fastapi import FastAPI
from datetime import datetime
import socket
import pickle
import pandas as pd
import os

app = FastAPI()

@app.get('/predict')
def predict(date_str: str):
    predicted_price = load_and_predict_price(date_str)
    return {'date': date_str, 'predicted_price': predicted_price}

def load_and_predict_price(date_str):
    with open('linear_regression_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    date = datetime.strptime(date_str, '%m/%d/%Y')
    date_features = pd.DataFrame([[date.year, date.month, date.day]], columns=['Year', 'Month', 'Day'])
    predicted_price = loaded_model.predict(date_features)
    return predicted_price[0]

if __name__ == '__main__':
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"Aplicación corriendo en http://{host_ip}:8000")
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


