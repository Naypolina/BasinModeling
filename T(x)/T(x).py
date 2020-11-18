import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

T_0 = 20
L = 10
Theta_0 = 0.5

x = np.linspace(0, L, 200)
y = T_0 + Theta_0 * np.sin(np.pi/L * x)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth = 2)
ax.grid()

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

ax.grid(which = 'major',
        color = 'k')
ax.grid(which = 'minor',
        color = 'gray',
        linestyle = ':')

ax.set_xlabel('Координата в образце (см)')
ax.set_ylabel('Температура (ºC)')

plt.show()