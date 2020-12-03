import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# параметры образца
L = 10
T_0 = 20
Theta_0 = 5
N = 3000
M = 50

# шаги переменных
t = 10
h = L/M

# константы для мрамора (брала средние значения в диапазоне)
c = 850
rho = 2.3
Lambda = 2.8
a = Lambda/(c*rho)

T = np.array([[0] * M for i in range(N)]).astype('float64')

for m in range(0, M):
    T[0][m] = T_0 + Theta_0 * np.sin(np.pi / L * m * h)

for n in range(1, N):
    T[n][0] = T_0
    T[n][M - 1] = T_0

for i, ti in enumerate(T):
    if i>0:
        ti[1:-1] = T[i-1][1:-1]+a*t/(h**2)*(T[i-1][:-2]-2*T[i-1][1:-1]+T[i-1][2:])
        # print(T[n][m])

x = []
y = []
z = []

for n in range(0, N):
    x.append([])
    y.append([])
    z.append([])
    for m in range(0, M):
        x[-1].append(m * h)
        y[-1].append(n * t)
        z[-1].append(T[n][m])

x = np.array(x)
y = np.array(y)
z = np.array(z)


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Температура (ºС)')
plt.show()


