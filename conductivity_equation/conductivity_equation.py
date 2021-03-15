import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.integrate as integrate
from mpl_toolkits.mplot3d import Axes3D

# параметры образца
L = 10
T_0 = 20
Theta_0 = 5
N = 10000
M = 50

# шаги переменных
tau = 3
h = L/(M - 1)

# константы для мрамора
c1 = 850
rho1 = 2.3
Lambda1 = 2.8
a1 = Lambda1/(c1*rho1)

# константы для глины
c2 = 180
rho2 = 1.9
Lambda2 = 1.7
a2 = Lambda2/(c2*rho2)

# численное решение уравнения теплопролводности для одного слоя
T = np.zeros([N,M])

for m in range(0, M):
    T[0][m] = T_0 + Theta_0 * np.sin(np.pi / L * m * h)

for n in range(1, N):
    T[n][0] = T_0
    T[n][-1] = T_0

for i, ti in enumerate(T):
    if i>0:
        ti[1:-1] = T[i-1][1:-1] + a1*tau/(h**2) * (T[i-1][:-2] - 2 * T[i-1][1:-1] + T[i-1][2:])

# численное решение уравнения теплопроводности для двух слоев
T2 = np.zeros([N, 2 * M])

for m in range(0, 2 * M):
    T2[0][m] = T_0 + Theta_0 * np.sin(np.pi / (2*L) * m * h)

for n in range(1, N):
    T2[n][0] = T_0
    T2[n][-1] = T_0

for i, ti in enumerate(T2):
    if i > 0:
        ti[1:M] = T2[i - 1][1:M] + a1 * tau / (h ** 2) * (T2[i - 1][:M-1] - 2 * T2[i - 1][1:M] + T2[i - 1][2:M+1])
        ti[M:-1] = T2[i - 1][M:-1] + a2 * tau / (h ** 2) * (T2[i - 1][M-1:-2] - 2 * T2[i - 1][M:-1] + T2[i - 1][M+1:])

# аналитическое решение уравнения теплопролводности
def T_an(x, t):
    return T_0 + Theta_0 * np.exp(- (np.pi / L) ** 2 * a1 * t) * np.sin(np.pi * x / L)

# заполнение массива значениями аналитического решения
T_aran = np.zeros([N,M])
for n in range(0, N):
    for m in range(0, M):
        T_aran[n][m] = T_an(m * h, n * tau)

# заполнение массива с разницей между численным и аналитическим решением
T_diff = np.array([[0] * M for i in range(N)]).astype('float64')
T_diff = np.abs(T_aran - T)


x = []
y = []
x2 = []
y2 = []
z1 = []
z2 = []
z3 = []
z4 = []

for n in range(0, N):
    x.append([])
    y.append([])
    x2.append([])
    y2.append([])
    z1.append([])
    z2.append([])
    z3.append([])
    z4.append([])
    for m in range(0, M):
        x[-1].append(m * h)
        y[-1].append(n * tau)
        z1[-1].append(T[n][m])
        z2[-1].append(T_aran[n][m])
        z3[-1].append(T_diff[n][m])
    for m in range(0, 2 * M):
        x2[-1].append(m * h)
        y2[-1].append(n * tau)
        z4[-1].append(T2[n][m])


x = np.array(x)
y = np.array(y)
x2 = np.array(x2)
y2 = np.array(y2)
z1 = np.array(z1)
z2 = np.array(z2)
z3 = np.array(z3)
z4 = np.array(z4)

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
ax.plot_surface(x, y, z3, color='grey')
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Разница температур (ºС)')

fig = plt.figure(4)
ax = plt.axes(projection="3d")
ax.plot_surface(x2, y2, z4, color='cyan')
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Распределение температур для двух слоев (ºС)')
plt.show()
