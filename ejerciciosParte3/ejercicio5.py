import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv(r'ERD\ERD\ejerciciosParte3\turismo_baleares.csv')

print(datos.head())

plt.bar(datos["Mes"], datos["Visitantes"], color="skyblue")
plt.title("Número de visitantes por mes en Baleares")
plt.xlabel("Meses")
plt.ylabel("Visitantes")
plt.xticks(rotation=45)
plt.savefig(r'ERD\ERD\ejerciciosParte3\visitantes_barras.png')
plt.show()

plt.plot(datos["Mes"], datos["Gasto_medio"], marker="o", color="green", label="Gasto medio (€)")
plt.title("Evolución del gasto medio mensual")
plt.xlabel("Meses")
plt.ylabel("Gasto medio (€)")
plt.legend()
plt.grid(True)
plt.savefig(r'ERD\ERD\ejerciciosParte3\gasto_lineas.png')
plt.show()

plt.pie(datos["Estancia_media"], labels=datos["Mes"], autopct="%1.1f%%", colors=plt.cm.Paired.colors)
plt.title("Distribución de la estancia media por mes")
plt.savefig(r'ERD\ERD\ejerciciosParte3\estancia_sectores.png')
plt.show()



