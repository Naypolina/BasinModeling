import numpy as np
import conditions as cond


# выбор шага по времени
tau = cond.tau([cond.a(cond.T_0)])

# численное решение уравнения теплопролводности
T = np.zeros([cond.N, cond.M + 1])
a_T = np.zeros(cond.M + 1)

m = np.arange(cond.M + 1)
T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / cond.L * m * cond.h)
T[:, 0] = cond.T_0
T[:, -1] = cond.T_0

for i, ti in enumerate(T):
    if i > 0:
        a_T = cond.a((T[i-1][:-1] + T[i-1][1:]) / 2)
        ti[1:-1] = T[i-1][1:-1] + tau / (cond.h ** 2) \
                   * (a_T[:-1] * T[i-1][:-2] - (a_T[:-1] + a_T[1:]) * T[i-1][1:-1] + a_T[1:] * T[i-1][2:])