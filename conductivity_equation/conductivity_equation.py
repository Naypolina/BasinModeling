import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
# import pylab
# from mpl_toolkits.mplot3d import Axes3D

# параметры образца
L = 10
T_0 = 20
Theta_0 = 5

# количество отрезков по времени
N = 10000
# количество отрезков по координате
M = 50

# константы для мрамора
c1 = 850
rho1 = 2.3
Lambda1 = 2.8
a1 = Lambda1 / (c1 * rho1)

# константы для глины
c2 = 180
rho2 = 1.9
Lambda2 = 1.7
a2 = Lambda2 / (c2 * rho2)

# константы для базальта
c3 = 840
rho3 = 2.9
Lambda3 = 0.47
a3 = Lambda3 / (c3 * rho3)

# шаги переменных с учетом проверки устойчивости схемы
tau = 3
h = L / M
if tau > pow(h, 2) / (2 * max(a1, a2, a3)):
    tau = pow(h, 2) // (2 * max(a1, a2, a3))


# численное решение уравнения теплопролводности для одного слоя
T = np.zeros([N, M + 1])

m = np.arange(M + 1)
T[0][m] = T_0 + Theta_0 * np.sin(np.pi / L * m * h)
T[:, 0] = T_0
T[:, -1] = T_0

for i, ti in enumerate(T):
    if i > 0:
        ti[1:-1] = T[i-1][1:-1] + a1*tau/(h**2) * (T[i-1][:-2] - 2 * T[i-1][1:-1] + T[i-1][2:])


# численное решение уравнения теплопроводности для двух слоев
T2 = np.zeros([N, 2 * M + 1])

m = np.arange(2 * M + 1)
T2[0][m] = T_0 + Theta_0 * np.sin(np.pi / (2 * L) * m * h)
T2[:, 0] = T_0
T2[:, -1] = T_0

for i, ti in enumerate(T2):
    if i > 0:
        ti[1:M] = (T2[i - 1][1:M]
                   + a1 * tau / (h ** 2)
                   * (T2[i - 1][:M - 1] - 2 * T2[i - 1][1:M] + T2[i - 1][2:M + 1]))
        ti[M:-1] = (T2[i - 1][M:-1]
                    + a2 * tau / (h ** 2)
                    * (T2[i - 1][M - 1:-2] - 2 * T2[i - 1][M:-1] + T2[i - 1][M + 1:]))


# численное решение уравнения теплопроводности для трёх слоев
T3 = np.zeros([N, 3 * M + 1])

m = np.arange(3 * M + 1)
T3[0][m] = T_0 + Theta_0 * np.sin(np.pi / (3 * L) * m * h)
T3[:, 0] = T_0
T3[:, -1] = T_0

for i, ti in enumerate(T3):
    if i > 0:
        ti[1:M] = (T3[i - 1][1:M]
                   + a1 * tau / (h ** 2)
                   * (T3[i - 1][:M - 1] - 2 * T3[i - 1][1:M] + T3[i - 1][2:M + 1]))
        ti[M:(2 * M)] = (T3[i - 1][M:(2 * M)]
                         + a2 * tau / (h ** 2)
                         * (T3[i - 1][M - 1:(2 * M)-1] - 2 * T3[i - 1][M:(2 * M)] + T3[i - 1][M + 1:(2 * M)+1]))
        ti[(2 * M):-1] = (T3[i - 1][(2 * M):-1]
                          + a3 * tau / (h ** 2)
                          * (T3[i - 1][(2 * M)-1:-2] - 2 * T3[i - 1][(2 * M):-1] + T3[i - 1][(2 * M) + 1:]))


# аналитическое решение уравнения теплопролводности
def temp_analyt(x, t):
    return T_0 + Theta_0 * np.exp(- (np.pi / L) ** 2 * a1 * t) * np.sin(np.pi * x / L)


# заполнение массива значениями аналитического решения
T_analytical = np.zeros([N, M + 1])
for n in range(0, N):
    for m in range(0, M + 1):
        T_analytical[n][m] = temp_analyt(m * h, n * tau)


# заполнение массива с разницей между численным и аналитическим решением
T_diff = np.abs(T_analytical - T)

# отрисовка 3D графиков
x = []
y = []
x4 = []
y4 = []
x5 = []
y5 = []

for n in range(0, N):
    x.append([])
    y.append([])
    x4.append([])
    y4.append([])
    x5.append([])
    y5.append([])

    for m in range(0, M + 1):
        x[-1].append(m * h)
        y[-1].append(n * tau)

    for m in range(0, 2 * M + 1):
        x4[-1].append(m * h)
        y4[-1].append(n * tau)

    for m in range(0, 3 * M + 1):
        x5[-1].append(m * h)
        y5[-1].append(n * tau)


x = np.array(x)
y = np.array(y)
x4 = np.array(x4)
y4 = np.array(y4)
x5 = np.array(x5)
y5 = np.array(y5)

# график численного решения для одного слоя
plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, T, rcount=10, ccount=10)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Температура числ (ºС)')

# график аналитического решения для одного слоя
plt.figure(2)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, T_analytical, color='green', rcount=10, ccount=10)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Температура аналит (ºС)')

# график разницы между численным и аналитическим решением
plt.figure(3)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, T_diff*1000, color='grey', rcount=10, ccount=10)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Разница температур (ºС * 10^(-3))')

# график численного решения для двухслойного образца
plt.figure(4)
ax = plt.axes(projection="3d")
cm4 = LinearSegmentedColormap.from_list('red_blue', ['c', 'w', 'y'], 256)
ax.plot_surface(x4, y4, T2, color='cyan', cmap=cm4, rcount=20, ccount=20)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Распределение температур для двух слоев (ºС)')

# график численного решения для трехслойного образца
plt.figure(5)
ax = plt.axes(projection="3d")
cm5 = LinearSegmentedColormap.from_list('red_blue', ['b', 'w', 'r'], 256)
ax.plot_surface(x5, y5, T3, color='#11aa55', cmap=cm5, rcount=20, ccount=20)
ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Время (с)')
ax.set_zlabel('Распределение температур для трёх слоев (ºС)')

# отрисовка 2D графиков
x_lin1 = []
x_lin2 = []
x_lin3 = []

for m in range(0, M + 1):
    x_lin1.append(m * h)

for m in range(0, 2 * M + 1):
    x_lin2.append(m * h)

for m in range(0, 3 * M + 1):
    x_lin3.append(m * h)


def graph_setup(x_label, y_label, g_title, x_max):
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    plt.title(g_title, fontsize=16)
    plt.legend(fontsize=14, loc='upper right')
    plt.minorticks_on()
    plt.xlim([0., x_max])
    plt.ylim([20., 26.])
    plt.grid(which='major', color='#C0C0C0')
    plt.grid(which='minor', ls='--', color='#D3D3D3')


plt.figure(6)
plt.plot(x_lin1, T[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin1, T[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin1, T[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin1, T[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin1, T[N - 1], color='#008080', label='t = 10000 секунд')
graph_setup(r'$x (см)$', r'$T (ºС)$',
            'Распределение температур образце для разных моментов времени \n (численное решение)', 10)


plt.figure(7)
plt.plot(x_lin2, T2[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin2, T2[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin2, T2[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin2, T2[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin2, T2[N - 1], color='#008080', label='t = 10000 секунд')
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница мрамор/глина', linewidth=2)
graph_setup(r'$x (см)$', r'$T (ºС)$',
            'Распределение температур в двухслойном образце для разных моментов времени', 20)


plt.figure(8)
plt.plot(x_lin3, T3[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin3, T3[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin3, T3[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin3, T3[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin3, T3[N - 1], color='#008080', label='t = 10000 секунд')
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница мрамор/глина', linewidth=2)
plt.axvline(x=20, color='#BC8F8F', ls='--', label='граница глина/базальт', linewidth=2)
graph_setup(r'$x (см)$', r'$T (ºС)$', 'Распределение температур в трёхслойном образце для разных моментов времени', 30)

plt.show()
