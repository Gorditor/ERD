import pandas as pd
import matplotlib.pyplot as plt

alumnos = ['Ana', 'Luis', 'Marta', 'Jordi', 'Sofía', 'Carlos', 'Lucía', 'Pablo']
matematicas = [7.5, 6.0, 8.0, 5.5, 9.0, 4.5, 6.5, 7.0]
lengua = [8.0, 5.5, 7.5, 6.0, 8.5, 5.0, 7.0, 6.5]

df_notas = pd.DataFrame({
    'Alumno': alumnos,
    'Matemáticas': matematicas,
    'Lengua': lengua
})

plt.figure(figsize=(8,6))
plt.bar(df_notas['Alumno'], df_notas['Matemáticas'], label='Matemáticas')
plt.bar(df_notas['Alumno'], df_notas['Lengua'], bottom=df_notas['Matemáticas'], label='Lengua')
plt.title('Notas por asignatura (barras apiladas)')
plt.ylabel('Nota')
plt.legend()
plt.xticks(rotation=45)
plt.show()

dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
temp_min = [12, 13, 11, 14, 15, 13, 12]
temp_max = [22, 24, 23, 25, 26, 24, 23]

plt.figure(figsize=(8,6))
plt.plot(dias, temp_min, marker='o', label='Mínima', color='blue')
plt.plot(dias, temp_max, marker='o', label='Máxima', color='red')
plt.title('Temperaturas semanales')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()

altura = [160, 165, 170, 155, 180, 175, 168, 172]
peso = [55, 60, 65, 50, 75, 70, 62, 68]

plt.figure(figsize=(8,6))
plt.scatter(altura, peso, color='green')
plt.title('Relación entre altura y peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.show()

notas_medias = [(m + l) / 2 for m, l in zip(matematicas, lengua)]

plt.figure(figsize=(8,6))
plt.hist(notas_medias, bins=5, color='purple', edgecolor='black')
plt.title('Distribución de notas medias')
plt.xlabel('Nota media')
plt.ylabel('Número de alumnos')
plt.show()

