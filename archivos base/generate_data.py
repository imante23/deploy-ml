import numpy as np
import pandas as pd

# Simulación de datos
np.random.seed(42)
tamaño = np.random.randint(50, 200, 500)  # Tamaño en m²
habitaciones = np.random.randint(1, 5, 500)  # Número de habitaciones
distancia = np.random.uniform(1, 20, 500)  # Distancia al centro

# Generar precios con ruido
precio = 3000 * tamaño + 10000 * habitaciones - 500 * distancia + np.random.normal(0, 50000, 500)

# Crear DataFrame
data = pd.DataFrame({
    'Tamaño_m2': tamaño,
    'Habitaciones': habitaciones,
    'Distancia_centro_km': distancia,
    'Precio': precio
})

# Guardar los datos
data.to_csv('datos_casas.csv', index=False)
