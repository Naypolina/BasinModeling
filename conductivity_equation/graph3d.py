import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import conditions as cond
import one_layer as l1
import two_layer as l2
import three_layer as l3

# отрисовка 3D графиков
x = []
y = []
x4 = []
y4 = []
x5 = []
y5 = []

for n in range(0, cond.N):
    x.append([])
    y.append([])
    x4.append([])
    y4.append([])
    x5.append([])
    y5.append([])

    for m in range(0, cond.M + 1):
        x[-1].append(m * cond.h)
        y[-1].append(n * cond.tau)

    for m in range(0, 2 * cond.M + 1):
        x4[-1].append(m * cond.h)
        y4[-1].append(n * cond.tau)

    for m in range(0, 3 * cond.M + 1):
        x5[-1].append(m * cond.h)
        y5[-1].append(n * cond.tau)


x = np.array(x)
y = np.array(y)
x4 = np.array(x4)
y4 = np.array(y4)
x5 = np.array(x5)
y5 = np.array(y5)

# график численного решения для одного слоя
plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.one_num(cond.a1), color='#5DB560')
ax.set_xlim(10, 0)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='z', labelsize=16)
ax.set_xlabel('x, см', fontsize=22, labelpad=15)
ax.set_ylabel('t, мин', fontsize=22, labelpad=20)
ax.set_zlabel('$T, ^{o}С$', fontsize=22, labelpad=15)

# график аналитического решения для одного слоя
plt.figure(2)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.T_analytical, color='#5491CE')
ax.set_xlim(10, 0)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='z', labelsize=16)
ax.set_xlabel('x, см', fontsize=22, labelpad=15)
ax.set_ylabel('t, мин', fontsize=22, labelpad=20)
ax.set_zlabel('$T, ^{o}С$', fontsize=22, labelpad=15)

# график разницы между численным и аналитическим решением
plt.figure(3)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.T_diff * 1000, color='#ED7E52')
ax.set_xlim(10, 0)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='z', labelsize=16, pad=5)
ax.set_xlabel('x, см', fontsize=22, labelpad=15)
ax.set_ylabel('t, мин', fontsize=22, labelpad=20)
ax.set_zlabel('$T, ^{o}С \cdot 10^{-3}$', fontsize=22, labelpad=20)

# # график численного решения для двухслойного образца
# plt.figure(4)
# ax = plt.axes(projection="3d")
# cm4 = LinearSegmentedColormap.from_list('red_blue', ['c', 'w', 'y'], 256)
# ax.plot_surface(x4, y4, l2.T, color='cyan', cmap=cm4, rcount=20, ccount=20)
# ax.set_xlabel('Координата в образце (см)')
# ax.set_ylabel('Время (с)')
# ax.set_zlabel('Распределение температур для двух слоев (ºС)')
#
# # график численного решения для трехслойного образца
# plt.figure(5)
# ax = plt.axes(projection="3d")
# cm5 = LinearSegmentedColormap.from_list('red_blue', ['b', 'w', 'r'], 256)
# ax.plot_surface(x5, y5, l3.T, color='#11aa55', cmap=cm5, rcount=20, ccount=20)
# ax.set_xlabel('Координата в образце (см)', fontsize=26)
# ax.set_ylabel('Время (с)', fontsize=26)
# ax.set_zlabel('Распределение температур для трёх слоев (ºС)', fontsize=26)

plt.show()
