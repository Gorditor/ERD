import numpy as np
import matplotlib.pyplot as plt

horas_estudio = np.random.uniform(0, 10, 50)

notes = horas_estudio * 0.5 + np.random.normal(5, 1, 50)

plt.scatter(horas_estudio, notes)
plt.title("Relación entre horas de estudio y notas")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota obtenida")
plt.grid(True)
plt.show()



