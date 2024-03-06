# параметры образца
L = 10
T_0 = 20
Theta_0 = 5

# количество отрезков по времени
N = 10000
# количество отрезков по координате
M = 50

# константы для известняка
c1 = 920  # Дж / (кг * К)
rho1 = 2.1  # г / см^3
Lambda1 = 2.56  # Вт / (м * К)
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

# константы для н-пентана
c_p = 2280
rho_p = 0.626
Lambda_p = 0.114
a_p = Lambda_p / (c_p * rho_p)

# пористость
phi = 0.4

# коэффициенты с учётом пористости
# поры заполненные воздухом
a_phi_air = pow(Lambda1, 1 - phi) * pow(Lambda_air, phi) / (c1 * (1 - phi) + c_air * phi) \
            / (rho1 * (1 - phi) + rho_air * phi)
# поры заполненные водой
a_phi_w = pow(Lambda1, 1 - phi) * pow(Lambda_w, phi) / (c1 * (1 - phi) + c_w * phi) \
          / (rho1 * (1 - phi) + rho_w * phi)

# функциональная зависимость теплопроводности от температуры (известняк)
def a(temp):
    Lambda = 9.03 * pow(temp, -0.25)
    return Lambda / (c1 * rho1)


# шаги переменных с учетом проверки устойчивости схемы
tau_init = 3
h = L / M


# функция проверки шага по времени
# на вход подается список из коэффициентов a, используемых при решении
def tau(a_list):
    if tau_init > pow(h, 2) / (2 * max(a_list)):
        return pow(h, 2) // (2 * max(a_list))
    else:
        return tau_init
