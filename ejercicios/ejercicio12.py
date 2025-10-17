import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Visual\ERD\ejercicios\ventas.csv')

plt.bar(df['Mes'], df['Ventas'])
plt.title('Ventas de enero a junio')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()

plt.plot(df['Mes'], df['Ventas'], marker='o')
plt.title('Evolución de las ventas')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()

plt.hist(df['Ventas'], bins=6)
plt.title('Distribución de las ventas')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.show()







