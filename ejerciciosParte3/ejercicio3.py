import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv(r'ERD\ERD\ejerciciosParte3\notes.csv')

notas['Media'] = notas[['Matemáticas','Catalán','Inglés']].mean(axis=1)

plt.figure(figsize=(8,6))
plt.bar(notas['Nombre'], notas['Media'], color='skyblue')
plt.title("Nota media por alumno")
plt.xlabel("Alumno")
plt.ylabel("Nota media")
plt.show()

encuesta = pd.Series({
    "Me gusta Python": 50,
    "Prefiero JavaScript": 30,
    "Me es indiferente": 20
})

plt.figure(figsize=(7,7))
encuesta.plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title("Resultados de la encuesta")
plt.ylabel("")
plt.show()

ventas = pd.DataFrame({
    "Semana": range(1,6),
    "Producto_A": [50, 60, 55, 70, 65],
    "Producto_B": [40, 45, 50, 55, 60],
    "Producto_C": [30, 35, 40, 38, 45]
})

plt.figure(figsize=(8,6))
plt.plot(ventas['Semana'], ventas['Producto_A'], marker='o', label='Producto A', color='blue')
plt.plot(ventas['Semana'], ventas['Producto_B'], marker='o', label='Producto B', color='red')
plt.plot(ventas['Semana'], ventas['Producto_C'], marker='o', label='Producto C', color='green')
plt.title("Ventas semanales por producto")
plt.xlabel("Semana")
plt.ylabel("Unidades vendidas")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=notas[['Matemáticas','Catalán','Inglés']])
plt.title("Distribución de notas por asignatura")
plt.ylabel("Nota")
plt.show()


