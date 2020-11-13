import numpy as np
import matplotlib.pyplot as plt

print("График синуса имеет вид: y = A * sin(omega * x + phi0).")
print("Введите соответсвующие параметры функции.")

A = float(input("A = "))
omega = float(input("omega = "))
phi0 = float(input("phi0 = "))

x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 200)
y = A * np.sin(omega * x + phi0)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()
plt.show()





