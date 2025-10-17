import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [1200, 950, 1100, 1300, 1250, 1400]

plt.plot(meses, ventas, color='darkred', linewidth=2.5, marker='s', markersize=8, label='Ventas 2025')
plt.title('Ventas del primer semestre', fontsize=14, fontweight='bold')
plt.suptitle('Análisis mensual de ingresos', fontsize=10)
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.legend()
plt.savefig(r'C:\Visual\ERD\ejercicios\graf.png')
plt.show()
