import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import datetime
import numpy as np
import pickle

# Cargar el conjunto de datos
df = pd.read_csv(r'C:\Users\asdel\OneDrive\Documentos\Contenedor\bitcoin_mlops_proyecto\data\btc_historical_dataset.csv')

# Convertir la columna de fecha a tipo datetime y ordenar el dataframe por esta columna
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Ingeniería de características: extraer año, mes y día
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Definir la variable objetivo y las características
X = df[['Year', 'Month', 'Day']]
y = df['Price']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
error = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio: {error}')

# Función para predecir el precio en una fecha dada
def predict_price(date):
    date = datetime.strptime(date, '%m/%d/%Y')
    date_features = np.array([[date.year, date.month, date.day]])
    predicted_price = model.predict(date_features)
    return predicted_price[0]

# Ejemplo de uso de la función
predicted_price = predict_price('10/25/2025')
print(f'Precio predicho para el 25/10/2025: {predicted_price}')

# Función para predecir el precio en una fecha dada
def predict_price(date_str):
    date = datetime.strptime(date_str, '%m/%d/%Y')
    date_features = pd.DataFrame([[date.year, date.month, date.day]], columns=['Year', 'Month', 'Day'])
    predicted_price = model.predict(date_features)
    return predicted_price[0]

# Guardar el modelo en un archivo pickle
with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Solicitar al usuario que ingrese la fecha
user_date = input("Por favor, ingrese la fecha en formato MM/DD/YYYY para predecir el precio del Bitcoin: ")

# Llamar a la función con la fecha ingresada por el usuario
predicted_price = predict_price(user_date)
print(f'Precio predicho para {user_date}: ${predicted_price:.2f}')

def load_and_predict_price(date_str):
    with open('linear_regression_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    date = datetime.strptime(date_str, '%m/%d/%Y')
    date_features = pd.DataFrame([[date.year, date.month, date.day]], columns=['Year', 'Month', 'Day'])
    predicted_price = loaded_model.predict(date_features)
    return predicted_price[0]

