import numpy as np
import conditions as cond


# выбор шага по времени
tau = cond.tau([cond.a1, cond.a2])

def two_num(a1, a2):
    # численное решение уравнения теплопроводности для двух слоев
    T = np.zeros([cond.N, 2 * cond.M + 1])

    m = np.arange(2 * cond.M + 1)
    T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / (2 * cond.L) * m * cond.h)
    T[:, 0] = cond.T_0
    T[:, -1] = cond.T_0

    for i, ti in enumerate(T):
        if i > 0:
            ti[1:cond.M] = (T[i - 1][1:cond.M]
                            + a1 * tau / (cond.h ** 2)
                            * (T[i - 1][:cond.M - 1] - 2 * T[i - 1][1:cond.M] + T[i - 1][2:cond.M + 1]))
            ti[cond.M:-1] = (T[i - 1][cond.M:-1]
                             + a2 * tau / (cond.h ** 2)
                             * (T[i - 1][cond.M - 1:-2] - 2 * T[i - 1][cond.M:-1] + T[i - 1][cond.M + 1:]))
    return T
