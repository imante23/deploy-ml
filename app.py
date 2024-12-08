from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('modelo_precio.pkl')

@app.route('/')
def home():
    return "Bienvenido a la API de predicción de precios. Usa la ruta '/predict' con una solicitud POST."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tamaño = data['Tamaño_m2']
    habitaciones = data['Habitaciones']
    distancia = data['Distancia_centro_km']
    
    prediction = model.predict([[tamaño, habitaciones, distancia]])
    return jsonify({'Precio_predicho': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

