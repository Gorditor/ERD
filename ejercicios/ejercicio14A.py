import matplotlib.pyplot as plt

productos = ['A', 'B', 'C', 'D']
ventas = [120, 80, 150, 100]

#El gráfico de barras enseña mejor la diferencia entre productos por lo que es mejor para comparar.
plt.figure(figsize=(6,4))
plt.bar(productos, ventas, color='skyblue')
plt.title('Ventas por producto (barras)')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.show()

#El gráfico circular sirve para ver mejro las proporciones.
plt.figure(figsize=(6,6))
plt.pie(ventas, labels=productos, autopct='%1.1f%%', startangle=90)
plt.title('Ventas por producto (circular)')
plt.show()


