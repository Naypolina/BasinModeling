import numpy as np
import conditions as cond

# численное решение уравнения теплопроводности для трёх слоев
T = np.zeros([cond.N, 3 * cond.M + 1])

m = np.arange(3 * cond.M + 1)
T[0][m] = cond.T_0 + cond.Theta_0 * np.sin(np.pi / (3 * cond.L) * m * cond.h)
T[:, 0] = cond.T_0
T[:, -1] = cond.T_0

for i, ti in enumerate(T):
    if i > 0:
        ti[1:cond.M] = (T[i - 1][1:cond.M]
                   + cond.a1 * cond.tau / (cond.h ** 2)
                   * (T[i - 1][:cond.M - 1] - 2 * T[i - 1][1:cond.M] + T[i - 1][2:cond.M + 1]))
        ti[cond.M:(2 * cond.M)] = (T[i - 1][cond.M:(2 * cond.M)]
                         + cond.a2 * cond.tau / (cond.h ** 2)
                         * (T[i - 1][cond.M - 1:(2 * cond.M)-1] - 2 * T[i - 1][cond.M:(2 * cond.M)] +
                         + T[i - 1][cond.M + 1:(2 * cond.M)+1]))
        ti[(2 * cond.M):-1] = (T[i - 1][(2 * cond.M):-1]
                          + cond.a3 * cond.tau / (cond.h ** 2)
                          * (T[i - 1][(2 * cond.M)-1:-2] - 2 * T[i - 1][(2 * cond.M):-1] + T[i - 1][(2 * cond.M) + 1:]))