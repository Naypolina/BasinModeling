import numpy as np
import conditions as cond


def a(x):
    return cond.a1 * (1 + (x / cond.L) ** 6)


# численное решение уравнения теплопролводности для одного слоя
T = np.zeros([cond.N, cond.M + 1])
a_x = np.zeros(cond.M + 1)

m = np.arange(cond.M + 1)
T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / cond.L * m * cond.h)
T[:, 0] = cond.T_0
T[:, -1] = cond.T_0
a_x[m] = a(m * cond.h + cond.h / 2)

for i, ti in enumerate(T):
    if i > 0:
        ti[1:-1] = T[i-1][1:-1] + cond.tau / (cond.h ** 2) \
                   * (a_x[:-2] * T[i-1][:-2] - (a_x[:-2] + a_x[2:]) * T[i-1][1:-1] + a_x[2:] * T[i-1][2:])

