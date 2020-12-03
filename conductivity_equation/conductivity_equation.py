import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.integrate as integrate
from mpl_toolkits.mplot3d import Axes3D

# параметры образца
L = 10
T_0 = 20
Theta_0 = 5
N = 3000
M = 50

# шаги переменных
tau = 10
h = L/(M - 1)

# константы для мрамора (брала средние значения в диапазоне)
c = 850
rho = 2.3
Lambda = 2.8
a = Lambda/(c*rho)

# численное решение уравнения теплопролводности
T = np.array([[0] * M for i in range(N)]).astype('float64')

for m in range(0, M):
    T[0][m] = T_0 + Theta_0 * np.sin(np.pi / L * m * h)

for n in range(1, N):
    T[n][0] = T_0
    T[n][M - 1] = T_0

for i, ti in enumerate(T):
    if i>0:
        ti[1:-1] = T[i-1][1:-1] + a*tau/(h**2) * (T[i-1][:-2] - 2 * T[i-1][1:-1] + T[i-1][2:])

# аналитическое решение уравнения теплопролводности
def T_an(x, t):
    return T_0 + Theta_0 * np.exp(- (np.pi / L) ** 2 * a * t) * np.sin(np.pi * x / L)

T_aran = np.array([[0] * M for i in range(N)]).astype('float64')
for n in range(0, N):
    for m in range(0, M):
        T_aran[n][m] = T_an(m * h, n * tau)

T_diff = np.array([[0] * M for i in range(N)]).astype('float64')
T_diff = np.abs(T_aran - T)

x = []
y = []
z1 = []
z2 = []
z3 = []

for n in range(0, N):
    x.append([])
    y.append([])
    z1.append([])
    z2.append([])
    z3.append([])
    for m in range(0, M):
        x[-1].append(m * h)
        y[-1].append(n * tau)
        z1[-1].append(T[n][m])
        z2[-1].append(T_aran[n][m])
        z3[-1].append(T_diff[n][m])


x = np.array(x)
y = np.array(y)
z1 = np.array(z1)
z2 = np.array(z2)
z3 = np.array(z3)

fig = plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z1)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Температура числ (ºС)')

fig = plt.figure(2)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z2, color='green')
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Температура аналит (ºС)')

fig = plt.figure(3)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z3, color='yellow')
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Разница температур (ºС)')
plt.show()
