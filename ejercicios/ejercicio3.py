import matplotlib.pyplot as plt

navegadores = 'Chrome', 'Firefox', 'Safari', 'Altres'
sizes = [65, 20, 10, 5]

fig, ax = plt.subplots()
ax.pie(sizes, labels=navegadores)
plt.show()


