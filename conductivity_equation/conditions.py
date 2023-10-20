# параметры образца
L = 10
T_0 = 20
Theta_0 = 5

# количество отрезков по времени
N = 10000
# количество отрезков по координате
M = 50

# константы для мрамора
c1 = 850
rho1 = 2.3
Lambda1 = 2.8
a1 = Lambda1 / (c1 * rho1)

# константы для глины
c2 = 180
rho2 = 1.9
Lambda2 = 1.7
a2 = Lambda2 / (c2 * rho2)

# константы для базальта
c3 = 840
rho3 = 2.9
Lambda3 = 0.47
a3 = Lambda3 / (c3 * rho3)

# шаги переменных с учетом проверки устойчивости схемы
tau = 3
h = L / M
if tau > pow(h, 2) / (2 * max(a1, a2, a3)):
    tau = pow(h, 2) // (2 * max(a1, a2, a3))