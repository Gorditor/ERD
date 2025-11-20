import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1, 31)
minutos_ejercicio = np.random.randint(20, 90, size=30)

plt.hist(minutos_ejercicio, bins=8, color="lightgreen", edgecolor="black")
plt.title("Distribución de minutos de ejercicio en 30 días")
plt.xlabel("Minutos de ejercicio")
plt.ylabel("Frecuencia")
plt.show()

plt.plot(dias, minutos_ejercicio, marker="o", color="blue")
plt.title("Evolución diaria de minutos de ejercicio")
plt.xlabel("Días")
plt.ylabel("Minutos de ejercicio")
plt.grid(True)
plt.show()

meses = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
ingresos = [2000, 2100, 1900, 2200, 2500, 2400, 2300, 2100, 2000, 2200, 2100, 2300]
gastos =   [1500, 1600, 1400, 1700, 1800, 1750, 1600, 1550, 1500, 1650, 1600, 1700]

plt.bar(meses, ingresos, label="Ingresos", color="green")
plt.bar(meses, gastos, label="Gastos", color="red", bottom=ingresos)
plt.title("Comparación de ingresos y gastos mensuales")
plt.xlabel("Meses")
plt.ylabel("Cantidad (€)")
plt.legend()
plt.show()

ahorro_mensual = np.array(ingresos) - np.array(gastos)
ahorro_acumulado = np.cumsum(ahorro_mensual)

plt.plot(meses, ahorro_acumulado, marker="o", color="purple")
plt.title("Ahorro acumulado durante el año")
plt.xlabel("Meses")
plt.ylabel("Ahorro acumulado (€)")
plt.grid(True)
plt.show()

temp_min = [5, 6, 8, 10, 13, 17, 20, 21, 18, 14, 9, 6]
temp_max = [15, 16, 18, 20, 24, 28, 31, 32, 28, 23, 18, 16]

plt.plot(meses, temp_min, marker="o", color="blue", label="Temperatura mínima")
plt.plot(meses, temp_max, marker="o", color="red", label="Temperatura máxima")
plt.title("Temperaturas mínimas y máximas por mes")
plt.xlabel("Meses")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

temp_media = (np.array(temp_min) + np.array(temp_max)) / 2
plt.bar(meses, temp_media, color="orange")
plt.title("Temperatura media mensual")
plt.xlabel("Meses")
plt.ylabel("Temperatura media (°C)")
plt.show()


