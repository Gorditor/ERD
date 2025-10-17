import matplotlib.pyplot as plt

mesos = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
temperatures = [22.5, 25, 27, 26, 28]

plt.plot(mesos, temperatures, marker="o", color="red")
plt.title("Temperaturas")
plt.xlabel("Meses")
plt.ylabel("Temperaturas")
plt.show()


