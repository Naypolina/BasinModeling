import numpy as np


# параметры образца
L = 10
T_0 = 20
Theta_0 = 5

# количество отрезков по времени
N = 10000
# количество отрезков по координате
M = 50

# константы для известняка
c1 = 920
rho1 = 2.1
Lambda1 = 2.56
a1 = Lambda1 / (c1 * rho1)

# константы для глины
c2 = 180
rho2 = 1.9
Lambda2 = 1.7
a2 = Lambda2 / (c2 * rho2)

# константы для сухого песка
c3 = 830
rho3 = 1.4
Lambda3 = 0.33
a3 = Lambda3 / (c3 * rho3)

# константы для воздуха
c_air = 720
rho_air = 0.0012
Lambda_air = 0.026
a_air = Lambda_air / (c_air * rho_air)

# константы для воды
c_w = 4200
rho_w = 1.0
Lambda_w = 0.56
a_w = Lambda_w / (c_w * rho_w)

# пористость
phi = 0.4

# коэффициенты с учётом пористости
# поры заполненные воздухом
a_phi_air = pow(Lambda1, 1 - phi) * pow(Lambda_air, phi) / (c1 * (1 - phi) + c_air * phi) \
            / (rho1 * (1 - phi) + rho_air * phi)
# поры заполненные водой
a_phi_w = pow(Lambda1, 1 - phi) * pow(Lambda_w, phi) / (c1 * (1 - phi) + c_w * phi) \
          / (rho1 * (1 - phi) + rho_w * phi)


# функциональная зависимость теплопроводности от глубины
def a(x):
    return Lambda1 * np.exp(-0.8 * x / L) / (c1 * rho1)


# шаги переменных с учетом проверки устойчивости схемы
tau = 3
h = L / M
if tau > pow(h, 2) / (2 * max(a1, a2, a3, a_phi_w, a_phi_air, a(L + h / 2))):
    tau = pow(h, 2) // (2 * max(a1, a2, a3, a_phi_w, a_phi_air, a(L + h / 2)))
