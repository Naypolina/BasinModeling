import numpy as np
import conditions as cond
import functions as f
import matplotlib.pyplot as plt

# начальная глубина (м)
L_0 = 2000
# длина отрезка по координате (м)
L = 1000
# число отрезков по координате
M = 200
# число отрезков по времени
N = 10000


# корреляционная зависимость пористости (в долях) от глубины (в м) для Западно-Сибирского бассейна
def phi(x):
    return (43.584 - 0.019 * x + 2.933 * 10 ** (-6) * x ** 2 - 1.508 * 10 ** (-10) * x ** 3) * 10**(-2)


# корреляционная зависимость теплопроводности от глубины (в м) для Западно-Сибирского бассейна
def lmbd(x):
    return 2.49 - 5 * phi(x)  # теплопроводность (Вт / (м * К))


# корреляционная зависимость плотности от глубины (в м) для Западно-Сибирского бассейна
def rho(x):
    return 0.34 * np.log(x + 590) - 0.216  # плотность (г/см^3)


# средняя теплоёмкость сухих пород Западно-Сибирского бассейна
def c(x):
    return 1030 * (1 - phi(x)) + 1000.5 * phi(x)  # теплоёмкость (Дж / (кг * К))


# функциональная зависимость темепературопроводности от глубины
# [x] = м, [a] = м^2 / ч
def a(x):
    return lmbd(x) / (c(x) * rho(x)) * 3600 / 1000


# шаг по координате
h = L / M  # м
# выбор шага по времени (КФЛ)
tau = h ** 2 // (2 * a(L_0 + L))  # ч

# численное решение с переменным коэффициентом a
T = np.zeros([N, M + 1])
m = np.arange(M + 1)
a_x = np.zeros(M + 1)

# начальное и граничные условия
T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / L * m * h)
T[:, 0] = cond.T_0
T[:, -1] = cond.T_0
a_x[m] = a(L_0 + m * h + h / 2)

for i, ti in enumerate(T):
    if i > 0:
        ti[1:-1] = T[i - 1][1:-1] + tau / (h ** 2) \
                   * (a_x[:-2] * T[i - 1][:-2] - (a_x[:-2] + a_x[2:]) * T[i - 1][1:-1] + a_x[2:] * T[i - 1][2:])

# численное решение с постоянным коффициентом a = a(2000 м)
Tc = np.zeros([N, M + 1])
m = np.arange(M + 1)

# начальное и граничные условия
Tc[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / L * m * h)
Tc[:, 0] = cond.T_0
Tc[:, -1] = cond.T_0

for i, ti in enumerate(Tc):
    if i > 0:
        ti[1:-1] = Tc[i-1][1:-1] + a(2000) * tau / (h ** 2) * (Tc[i-1][:-2] - 2 * Tc[i-1][1:-1] + Tc[i-1][2:])


# T(x, t) при a = a(x)
fig1, ax1 = plt.subplots()

x = np.linspace(L_0, L_0 + L + h, M + 1)

for i in range(5):
    # температурные кривые
    plt.plot(x, T[2000 * i],
                 color=f.colors1[i], label=str(int(round(2000 * i * tau / (24 * 365), -2))) + ' лет', linewidth=4)
    # максимумы температурных кривых
    plt.plot(L_0 + h * T[2000 * i].argmax(), max(T[2000 * i]), '-o', color='black')

# настройка подписей осей и пр.
f.plot_setup(r'$x, м$', r'$T, ^{o}С$',
             '', [2000., 3000.], [20., 26.], ax1, 200, 1)
# подпись материалов на графике
f.text_on_plot(ax1, 2100, 24.2, '$a = a(x)$')


# T(x, t) при a = const
fig2, ax2 = plt.subplots()
for i in range(5):
    # температурные кривые
    plt.plot(x, Tc[2000 * i],
                 color=f.colors1[i], label=str(int(round(2000 * i * tau / (24 * 365), -2))) + ' лет', linewidth=4)
    # максимумы температурных кривых
    plt.plot(L_0 + h * Tc[2000 * i].argmax(), max(Tc[2000 * i]), '-o', color='black')

# настройка подписей осей и пр.
f.plot_setup(r'$x, м$', r'$T, ^{o}С$',
             '', [2000., 3000.], [20., 26.], ax2, 200, 1)
# подпись материалов на графике
f.text_on_plot(ax2, 2100, 24.2, '$a = const$')

# построение графика разницы температур
fig3, ax3 = plt.subplots()
for i in range(5):
    plt.plot(x, (Tc - T)[2000 * i],
                 color=f.colors1[i], label=str(int(round(2000 * i * tau / (24 * 365), -2))) + ' лет', linewidth=4)
# настройка подписей осей и пр.
f.plot_setup(r'$x, м$', r'$T, ^{o}С$',
             '', [2000., 3000.], [-0.1, 0.2], ax3, 200, 0.05)


# построение графика a(x)
fig4, ax4 = plt.subplots()
plt.plot(x, a(x) * 1000, linewidth=4, color='#cc254c', label='$a(x)$')
# настройка подписей осей и пр.
f.plot_setup(r'$x, м$', r'$a \cdot 10^3, м^2 / ч$',
             '', [2000., 3000.], [2.4, 2.8], ax4, 200, 0.1)

plt.show()
