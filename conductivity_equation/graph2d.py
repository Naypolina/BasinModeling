import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import conditions as cond
import functions as f
import one_layer as l1
import two_layer as l2
import three_layer as l3


# отрисовка 2D графиков
x_lin1 = []
x_lin2 = []
x_lin3 = []

for m in range(0, cond.M + 1):
    x_lin1.append(m * cond.h)

for m in range(0, 2 * cond.M + 1):
    x_lin2.append(m * cond.h)

for m in range(0, 3 * cond.M + 1):
    x_lin3.append(m * cond.h)


plt.figure(1)
plt.plot(x_lin1, l1.T[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin1, l1.T[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin1, l1.T[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin1, l1.T[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin1, l1.T[cond.N - 1], color='#008080', label='t = 10000 секунд')
f.graph_setup(r'$x (см)$', r'$T (ºС)$',
            'Распределение температур образце для разных моментов времени \n (численное решение)', 10)


plt.figure(2)
plt.plot(x_lin2, l2.T[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin2, l2.T[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin2, l2.T[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin2, l2.T[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin2, l2.T[cond.N - 1], color='#008080', label='t = 10000 секунд')
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница мрамор/глина', linewidth=2)
f.graph_setup(r'$x (см)$', r'$T (ºС)$',
            'Распределение температур в двухслойном образце для разных моментов времени', 20)


plt.figure(3)
plt.plot(x_lin3, l3.T[0], color='#8B0000', label='t = 0 секунд')
plt.plot(x_lin3, l3.T[2500], color='#FF8C00', label='t = 2500 секунд')
plt.plot(x_lin3, l3.T[5000], color='#DAA520', label='t = 5000 секунд')
plt.plot(x_lin3, l3.T[7500], color='#228B22', label='t = 7500 секунд')
plt.plot(x_lin3, l3.T[cond.N - 1], color='#008080', label='t = 10000 секунд')
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница мрамор/глина', linewidth=2)
plt.axvline(x=20, color='#BC8F8F', ls='--', label='граница глина/базальт', linewidth=2)
f.graph_setup(r'$x (см)$', r'$T (ºС)$', 'Распределение температур в трёхслойном образце для разных моментов времени', 30)

plt.show()