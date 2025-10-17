import numpy as np
import matplotlib.pyplot as plt

jornades = np.arange(1, 21)
punts = np.random.randint(0, 4, size=20) 

millor_index = np.argmax(punts)
millor_jornada = jornades[millor_index]
millor_punts = punts[millor_index]

plt.plot(jornades, punts, marker='o', linestyle='-', color='blue', label='Puntos por jornada')

plt.plot(millor_jornada, millor_punts, 'ro', label='Mejor jornada')

plt.title('Evolución de los puntos del equipo')
plt.xlabel('Jornada')
plt.ylabel('Puntos ganados')
plt.legend()
plt.grid(True)
plt.show()



