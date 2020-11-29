import numpy as np
import matplotlib.pyplot as plt

# параметры образца
L = 10
T_0 = 20
Theta_0 = 5
N = 50
M = 50

# шаги переменных
t = 1
h = L/M

# константы для мрамора (брала средние значения в диапазоне)
c = 850
rho = 2.3
Lambda = 2.8
a = Lambda/(c*rho)

T = [[0] * M for i in range(N)]
for m in range(0, M):
    T[0][m] = T_0 + Theta_0 * np.sin(np.pi / L * m * h)

for n in range(1, N):
    T[n][0] = T_0
    T[n][M - 1] = T_0

for n in range(1, N):
    for m in range(1, M):
        T[n][m] = T[n - 1][m - 1] + a*t/(h**2) * (T[n - 1][m - 2] - 2 * T[n - 1][m - 1] + T[n - 1][m])
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


