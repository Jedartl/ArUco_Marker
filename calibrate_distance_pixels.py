#Prueba valores de pixeles
import numpy as np

# Define the number of data points to collect
cantidad = 40

# Create a NumPy array to store distance and pixel values
disxpix = np.zeros((2, cantidad))  # 2 rows (distance, pixels), 40 columns (data points)

# Collect data from the user
for i in range(cantidad - 1):
    # Prompt for distance value and store it in the array
    distance = float(input("Ingrese la distancia en cm: "))
    disxpix[0][i] = distance

    # Prompt for pixel value and store it in the array
    pixels = int(input("Ingrese la cantidad de pixeles: "))
    disxpix[1][i] = pixels

# Display the collected data
for i in range(cantidad - 1):
    print(f"Distancia {i+1}: {disxpix[0][i]} cm")
    print(f"Pixeles {i+1}: {disxpix[1][i]}")