import matplotlib.pyplot as plt

fruites = ["Manzanas", "Peras", "Plátanos", "Naranjas"]
persones = [57, 94, 23, 45]

bar_colors = ['tab:red','tab:blue','tab:green','tab:orange']

plt.bar(fruites, persones, color=bar_colors)
plt.title("Quien se la ha comido")
plt.xlabel("Tipos de fruta")
plt.ylabel("Nombre")
plt.show()

