import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

matematicas = np.random.uniform(1, 10, 50)
historia = np.random.uniform(1, 10, 50)
ingles = np.random.uniform(1, 10, 50)

notas = [matematicas, historia, ingles]
asignaturas = ['Matemáticas', 'Historia', 'Inglés']

sns.boxplot(data=notas)
plt.xticks([0, 1, 2], asignaturas)
plt.title("Distribucion de las notas")
plt.xlabel("Asignatura")
plt.ylabel("Nota")
plt.show()




