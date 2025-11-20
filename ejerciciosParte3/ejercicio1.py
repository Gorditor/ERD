import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

animales = pd.DataFrame({
    'Animal': ['León', 'Tigre', 'Elefante', 'Cebra', 'Jirafa', 'Mono'],
    'Ejemplares': [5, 3, 2, 7, 4, 10]
})

plt.figure(figsize=(8, 5))
plt.bar(animales['Animal'], animales['Ejemplares'], color='skyblue')
plt.title('Ejemplares por Animal en el Zoológico')
plt.xlabel('Animal')
plt.ylabel('Número de Ejemplares')
plt.tight_layout()
plt.show()

dias = pd.date_range(start='2025-11-01', periods=10)
precios = pd.Series([10.5, 10.7, 10.6, 10.8, 11.0, 11.2, 11.1, 11.3, 11.5, 11.4], index=dias)

plt.figure(figsize=(8, 5))
precios.plot(marker='o', linestyle='-', color='green')
plt.title('Evolución del Precio del Producto')
plt.xlabel('Fecha')
plt.ylabel('Precio (€)')
plt.grid(True)
plt.tight_layout()
plt.show()

horario = pd.Series({
    'Sueño': 56,
    'Clases': 30,
    'Ocio': 25,
    'Deporte': 10,
    'Estudio': 20,
    'Otros': 27
})

plt.figure(figsize=(7, 7))
horario.plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Distribución del Horario Semanal')
plt.ylabel('')
plt.tight_layout()
plt.show()

datos = np.random.randint(0, 21, size=100)

plt.figure(figsize=(8, 5))
plt.hist(datos, bins=10, color='salmon', edgecolor='black')
plt.title('Histograma de Números Aleatorios (0-20)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()



