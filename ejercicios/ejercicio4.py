import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import EventCollection

np.random.seed(19680801)

xdata = np.arange(1, 21)

ydata1 = np.random.randint(10, 100, size=20)
ydata2 = np.random.randint(10, 100, size=20)

ydata1 = np.sort(ydata1)
ydata2 = np.sort(ydata2)[::-1]  

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata, ydata1, color='tab:blue', label='Producto A')
ax.plot(xdata, ydata2, color='tab:red', label='Producto B')

xevents1 = EventCollection(xdata, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata, color='tab:red', linelength=0.05)

yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05, orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:red', linelength=0.05, orientation='vertical')

ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

ax.set_xlim([0, 21])
ax.set_ylim([0, 110])

ax.set_title('Comparación de precios de dos productos')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Precio')
ax.legend()

plt.show()
