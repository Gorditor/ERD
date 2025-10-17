import numpy as np
import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
ventas = [1200, 950, 1100, 1300, 1250, 1400]
distribucion = np.random.normal(1200, 150, 100)
x = np.random.randint(900, 1500, 50)
y = np.random.randint(1, 6, 50)

plt.figure(figsize=(12,8))

#1 Gráfico de barras
plt.subplot(2,2,1)
plt.bar(meses, ventas, color='orange')
plt.title('Ventas mensuales')

#2 Histograma
plt.subplot(2,2,2)
plt.hist(distribucion, bins=10, color='green', edgecolor='black')
plt.title('Distribución de ventas')

#3 Scatter plot
plt.subplot(2,2,3)
plt.scatter(x, y, color='purple')
plt.title('Relación entre ventas y categoría')

#4 Gráfico circular
plt.subplot(2,2,4)
plt.pie(ventas, labels=meses, autopct='%1.1f%%', startangle=90)
plt.title('Proporción de ventas por mes')

plt.tight_layout()
plt.show()
