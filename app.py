from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('modelo_precio.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tamaño = request.form['Tamaño_m2']
    habitaciones = request.form['Habitaciones']
    distancia = request.form['Distancia_centro_km']
    
    # Convertir los datos a float para la predicción
    tamaño = float(tamaño)
    habitaciones = int(habitaciones)
    distancia = float(distancia)

    # Hacer la predicción
    prediction = model.predict([[tamaño, habitaciones, distancia]])
    
    # Mostrar el resultado en la misma página
    return render_template('index.html', prediccion=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
















