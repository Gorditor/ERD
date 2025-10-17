import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

notes = np.random.uniform(4, 10, 50)

sns.histplot(notes, kde=True)
plt.title("Distribucion de les notas")
plt.xlabel("Nota")
plt.ylabel("Freqüencia")
plt.show()

