import numpy as np
import matplotlib.pyplot as plt


whatsapp = np.random.uniform(1, 10, 50)
instagram = np.random.uniform(1, 10, 50)
tiktok = np.random.uniform(1, 10, 50)
twitter = np.random.uniform(1, 10, 50)
facebook = np.random.uniform(1, 10, 50)

redes = 'WhatsApp','Instagram','TikTok','Facebook','Twitter'

usos = [
    whatsapp.sum(),
    instagram.sum(),
    tiktok.sum(),
    facebook.sum(),
    twitter.sum()
]

plt.figure(figsize=(6,6))
plt.pie(usos, labels=redes, autopct='%1.1f%%', startangle=90)
plt.title('Uso de redes sociales (gráfico circular)')
plt.show()

plt.figure(figsize=(8,5))
plt.bar(redes, usos, color='lightgreen')
plt.title('uso de redes sociales (grafico de barras)')
plt.xlabel('Red social')
plt.ylabel('Horas totales')
plt.show()



