import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Cargar datos
data = pd.read_csv('datos_casas.csv')
X = data[['Tamaño_m2', 'Habitaciones', 'Distancia_centro_km']]
y = data['Precio']

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, 'modelo_precio.pkl')
