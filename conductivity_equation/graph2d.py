import matplotlib.pyplot as plt
import numpy as np

import conditions as cond
import functions as f
import one_layer as l1
import two_layer as l2
import three_layer as l3


# отрисовка 2D графиков
x_lin1 = np.linspace(0, cond.L, cond.M + 1)
x_lin2 = np.linspace(0, 2 * cond.L, 2 * cond.M + 1)
x_lin3 = np.linspace(0, 3 * cond.L, 3 * cond.M + 1)

# шаг по времени
tau = cond.tau_init

# однородный образец
fig1, ax1 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a3)[2700 * i],
             color=f.colors1[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)
    plt.plot(cond.h * l1.one_num(cond.a3)[2700 * i].argmax(),
             max(l1.one_num(cond.a3)[2700 * i]), '-o', color='black')

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 50.], [20., 26.], ax1, 10, 1)
# подпись материалов на графике
f.text_on_plot(ax1, 5.2, 24.4, 'алевролит')


# двухслойный образец
fig2, ax2 = plt.subplots()

# вертикальные прямые на границах раздела
plt.axvline(x=cond.L, color='#2F4F4F', ls='--', linewidth=4) #,
            # label='граница\nизвестняк/\nалевролит')

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin2, l2.two_num(cond.a1, cond.a3)[2700 * i],
             color=f.colors1[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)
    plt.plot(cond.h * l2.two_num(cond.a1, cond.a3)[2700 * i].argmax(),
             max(l2.two_num(cond.a1, cond.a3)[2700 * i]), '-o', color='black')

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 100.], [20., 26.], ax2, 20, 1)
# подпись материалов на графике
f.text_on_plot(ax2, 7.8, 24.3, 'известняк')
f.text_on_plot(ax2, 56.7, 20.8, 'алевролит')


# трехслойный образец
fig3, ax3 = plt.subplots()

# вертикальные прямые на границах раздела
plt.axvline(x=cond.L, color='#2F4F4F', ls='--', linewidth=4) #,
            # label='граница\nизвестняк/\nглинистый сланец')
plt.axvline(x=2 * cond.L, color='#BC8F8F', ls='--', linewidth=4) #,
            # label='граница\nглинистый сланец/\n алевролит')

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin3, l3.three_num(cond.a1, cond.a2, cond.a3)[2700 * i],
             color=f.colors1[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)
    plt.plot(cond.h * l3.three_num(cond.a1, cond.a2, cond.a3)[2700 * i].argmax(),
             max(l3.three_num(cond.a1, cond.a2, cond.a3)[2700 * i]), '-o', color='black')

f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 150.], [20., 26.], ax3, 20, 1)

# подпись материалов на графике
f.text_on_plot(ax3, 12, 24.3, 'известняк')
f.text_on_plot(ax3, 65.5, 21.5, 'глинистый\nсланец')
f.text_on_plot(ax3, 106.5, 20.8, 'алевролит')


# однородный образец с учетом пористости (воздух)
fig4, ax4 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[2700 * i],
             color=f.colors2[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 50.], [20., 26.], ax4, 10, 1)
f.text_on_plot(ax4, 16.0, 20.3, 'содержимое пор: воздух')


# однородный образец с учетом пористости (н-пентан)
fig5, ax5 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_phi_p)[2700 * i],
             color=f.colors3[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 50.], [20., 26.], ax5, 10, 1)
f.text_on_plot(ax5, 14.2, 20.3, 'содержимое пор: н-пентан')


# однородный образец с учетом пористости (вода)
fig6, ax6 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_phi_w)[2700 * i],
             color=f.colors4[i], label=str(2700 * i * tau // 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 50.], [20., 26.], ax6, 10, 1)
f.text_on_plot(ax6, 16.5, 20.3, 'содержимое пор: вода')


# зависимость a(phi) для различных флюидов
# скелет породы -- известняк (c1, rho1, Lambda1)
phi = np.linspace(0., 0.2, 100)
fig7, ax7 = plt.subplots()

plt.plot(phi, cond.a_phi(phi, cond.rho1, cond.rho_w, cond.c1, cond.c_w, cond.Lambda1, cond.Lambda_w) * 1000,
         color='#1c19d1', label='вода', linewidth=4, ls='--')
plt.plot(phi, cond.a_phi(phi, cond.rho1, cond.rho_air, cond.c1, cond.c_air, cond.Lambda1, cond.Lambda_air) * 1000,
         color='#099136', label='воздух', linewidth=4, ls='dashdot')
plt.plot(phi, cond.a_phi(phi, cond.rho1, cond.rho_np, cond.c1, cond.c_np, cond.Lambda1, cond.Lambda_np) * 1000,
         color='#eb9413', label='н-пентан', linewidth=4)
f.plot_setup(r'$\varphi$', r'$a \cdot 10^{3}, см^{2} / с$',
             '', [0., 0.2], [6., 16.], ax7, 0.05, 2)
plt.legend(fontsize=24, loc='upper right', shadow=True, fancybox=True)
f.text_on_plot(ax7, 0.03, 7.4, 'порода: известняк')

# зависимость a(phi) для различных флюидов
# скелет породы -- глинистый сланец (c2, rho2, Lambda2)
fig8, ax8 = plt.subplots()

plt.plot(phi, cond.a_phi(phi, cond.rho2, cond.rho_w, cond.c2, cond.c_w, cond.Lambda2, cond.Lambda_w) * 1000,
         color='#1c19d1', label='вода', linewidth=4, ls='--')
plt.plot(phi, cond.a_phi(phi, cond.rho2, cond.rho_air, cond.c2, cond.c_air, cond.Lambda2, cond.Lambda_air) * 1000,
         color='#099136', label='воздух', linewidth=4, ls='dashdot')
plt.plot(phi, cond.a_phi(phi, cond.rho2, cond.rho_np, cond.c2, cond.c_np, cond.Lambda2, cond.Lambda_np) * 1000,
         color='#eb9413', label='н-пентан', linewidth=4)
f.plot_setup(r'$\varphi$', r'$a \cdot 10^{3}, см^{2} / с$',
             '', [0., 0.2], [4., 11.], ax8, 0.05, 2)
plt.legend(fontsize=24, loc='upper right', shadow=True, fancybox=True)
f.text_on_plot(ax8, 0.03, 4.9, 'порода:\nглинистый сланец')

# зависимость a(phi) для различных флюидов
# скелет породы -- алевролит (c3, rho3, Lambda3)
fig9, ax9 = plt.subplots()

plt.plot(phi, cond.a_phi(phi, cond.rho3, cond.rho_w, cond.c3, cond.c_w, cond.Lambda3, cond.Lambda_w) * 1000,
         color='#1c19d1', label='вода', linewidth=4, ls='--')
plt.plot(phi, cond.a_phi(phi, cond.rho3, cond.rho_air, cond.c3, cond.c_air, cond.Lambda3, cond.Lambda_air) * 1000,
         color='#099136', label='воздух', linewidth=4, ls='dashdot')
plt.plot(phi, cond.a_phi(phi, cond.rho3, cond.rho_np, cond.c3, cond.c_np, cond.Lambda3, cond.Lambda_np) * 1000,
         color='#eb9413', label='н-пентан', linewidth=4)
f.plot_setup(r'$\varphi$', r'$a \cdot 10^{3}, см^{2} / с$',
             '', [0., 0.2], [3., 7.], ax9, 0.05, 1)
plt.legend(fontsize=24, loc='upper right', shadow=True, fancybox=True)
f.text_on_plot(ax9, 0.03, 3.5, 'порода: алевролит')

plt.show()
