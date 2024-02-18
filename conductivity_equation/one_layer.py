import numpy as np
import conditions as cond


def one_num(a):
    # численное решение уравнения теплопролводности для одного слоя
    T = np.zeros([cond.N, cond.M + 1])

    m = np.arange(cond.M + 1)
    T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / cond.L * m * cond.h)
    T[:, 0] = cond.T_0
    T[:, -1] = cond.T_0

    for i, ti in enumerate(T):
        if i > 0:
            ti[1:-1] = T[i-1][1:-1] + a * cond.tau / (cond.h ** 2) * (T[i-1][:-2] - 2 * T[i-1][1:-1] + T[i-1][2:])
    return T


# аналитическое решение уравнения теплопролводности
def temp_analytical(x, t):
    return cond.T_0 + cond.Theta_0 * np.exp(- (np.pi / cond.L) ** 2 * cond.a1 * t) * np.sin(np.pi * x / cond.L)


# заполнение массива значениями аналитического решения
T_analytical = np.zeros([cond.N, cond.M + 1])
for n in range(0, cond.N):
    for m in range(0, cond.M + 1):
        T_analytical[n][m] = temp_analytical(m * cond.h, n * cond.tau)


# заполнение массива с разницей между численным и аналитическим решением
T_diff = np.abs(T_analytical - one_num(cond.a1))
