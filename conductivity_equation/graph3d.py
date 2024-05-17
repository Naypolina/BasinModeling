import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import conditions as cond
import one_layer as l1

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
        y[-1].append(n * cond.tau_init)

    for m in range(0, 2 * cond.M + 1):
        x4[-1].append(m * cond.h)
        y4[-1].append(n * cond.tau_init)

    for m in range(0, 3 * cond.M + 1):
        x5[-1].append(m * cond.h)
        y5[-1].append(n * cond.tau_init)


x = np.array(x)
y = np.array(y)
x4 = np.array(x4)
y4 = np.array(y4)
x5 = np.array(x5)
y5 = np.array(y5)

# график численного решения для одного слоя
plt.figure(1)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.one_num(cond.a3), color='#5DB560')
ax.set_xlim(cond.L, 0)
ax.tick_params(axis='x', labelsize=20, pad=5)
ax.tick_params(axis='y', labelsize=20, pad=5)
ax.tick_params(axis='z', labelsize=20, pad=5)
ax.set_xlabel('x, см', fontsize=24, labelpad=15)
ax.set_ylabel('t, мин', fontsize=24, labelpad=20)
ax.set_zlabel('$T, ^{o}С$', fontsize=24, labelpad=15)

# график аналитического решения для одного слоя
plt.figure(2)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.T_analytical, color='#5491CE')
ax.set_xlim(cond.L, 0)
ax.tick_params(axis='x', labelsize=20, pad=5)
ax.tick_params(axis='y', labelsize=20, pad=5)
ax.tick_params(axis='z', labelsize=20, pad=5)
ax.set_xlabel('x, см', fontsize=24, labelpad=15)
ax.set_ylabel('t, мин', fontsize=24, labelpad=20)
ax.set_zlabel('$T, ^{o}С$', fontsize=24, labelpad=15)

# график разницы между численным и аналитическим решением
plt.figure(3)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y / 60, l1.T_diff * 1000, color='#ED7E52')
ax.set_xlim(cond.L, 0)
ax.tick_params(axis='x', labelsize=20, pad=5)
ax.tick_params(axis='y', labelsize=20, pad=5)
ax.tick_params(axis='z', labelsize=20, pad=5)
ax.set_xlabel('x, см', fontsize=24, labelpad=15)
ax.set_ylabel('t, мин', fontsize=24, labelpad=20)
ax.set_zlabel('$T, ^{o}С \cdot 10^{-3}$', fontsize=24, labelpad=20)

plt.show()
