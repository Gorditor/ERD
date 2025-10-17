import matplotlib.pyplot as plt
import numpy as np

deportes = (
    "Fútbol",
    "Básquet",
    "Volley",
)
weight_counts = {
    "Niños": np.array([12, 10, 5]),
    "Niñas": np.array([6, 8, 12]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(deportes, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Número de niños y niñas por deporte")
ax.legend(loc="upper right")

plt.show()