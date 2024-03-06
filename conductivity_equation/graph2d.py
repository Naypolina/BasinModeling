import matplotlib.pyplot as plt

import conditions as cond
import functions as f
import one_layer as l1
import two_layer as l2
import three_layer as l3
import variable_coefficients as vc


# отрисовка 2D графиков
x_lin1 = []
x_lin2 = []
x_lin3 = []

for m in range(0, cond.M + 1):
    x_lin1.append(m * cond.h)

for m in range(0, 2 * cond.M + 1):
    x_lin2.append(m * cond.h)

for m in range(0, 3 * cond.M + 1):
    x_lin3.append(m * cond.h)

# цветовые палитры
colors1 = ['#8B0000', '#FF8C00', '#DAA520', '#228B22', '#008080']
colors2 = ['#cc254c', '#ab25cc', '#6525cc', '#2573cc', '#25a5cc']
colors3 = ['#d6432f', '#eb9413', '#dfe312', '#34b015', '#17bd96']
colors4 = ['#1c19d1', '#255ccc', '#259acc', '#25c1cc', '#25ccb8']

# однородный образец
fig1, ax1 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a1)[1800 * i],
             color=colors1[i], label=str(1800 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax1, (1, 1))
# подпись материалов на графике
f.text_on_plot(ax1, 0.7, 24.2, 'известняк')


# двухслойный образец
fig2, ax2 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin2, l2.two_num(cond.a1, cond.a2)[1800 * i],
             color=colors1[i], label=str(1800 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 20.], [20., 26.], ax2, (1.08, 1.05))
# вертикальные прямые на границах раздела
plt.axvline(x=10, color='#2F4F4F', ls='--',
            label='граница \n известняк/глина', linewidth=4)
# подпись материалов на графике
f.text_on_plot(ax2, 1.2, 23.67, 'известняк')
f.text_on_plot(ax2, 13.3, 24.67, 'глина')


# трехслойный образец
fig3, ax3 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin3, l3.three_num(cond.a1, cond.a2, cond.a3)[2400 * i],
             color=colors1[i], label=str(2400 * i / 60) + ' минут', linewidth=4)

f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 30.], [20., 26.], ax3, (1.15, 1.05))
# вертикальные прямые на границах раздела
plt.axvline(x=10, color='#2F4F4F', ls='--',
            label='граница \n известняк/глина', linewidth=4)
plt.axvline(x=20, color='#BC8F8F', ls='--',
            label='граница \n глина/песок', linewidth=4)
# подпись материалов на графике
f.text_on_plot(ax3, 0.8, 23.5, 'известняк')
f.text_on_plot(ax3, 13.5, 22.17, 'глина')
f.text_on_plot(ax3, 21, 21.25, 'сухой\nпесок')

# функциональная зависимость от глубины
fig4, ax4 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, vc.T[900 * i],
             color=colors1[i], label=str(900 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax4, (1, 1))
# подпись материалов на графике
f.text_on_plot(ax4, 0.7, 24.2, 'известняк \n ($\lambda(T)$)')


# однородный образец (сравнение с функциональной зависимостью)
fig5, ax5 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a(cond.T_0))[900 * i],
             color=colors1[i], label=str(900 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax5, (1, 1))
# подпись материалов на графике
f.text_on_plot(ax5, 0.7, 24.2, 'известняк \n ($\lambda = const$)')


# сравнение на одном графике
fig6, ax6 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, vc.T[900 * i] - l1.one_num(cond.a(cond.T_0))[900 * i],
             color=colors1[i], label=str(900 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [-0.005, 0.05], ax6, (1, 1))

# однородный образец с учетом пористости (воздух)
fig7, ax7 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[1800 * i],
             color=colors2[i], label=str(1800 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax7, (1, 1))
f.text_on_plot(ax7, 2.95, 20.75, 'содержимое пор: воздух')


# однородный образец с учетом пористости (н-пентан)
fig8, ax8 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_p)[1800 * i],
             color=colors3[4-i], label=str(1800 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax8, (1, 1))
f.text_on_plot(ax8, 2.8, 21.4, 'содержимое пор: н-пентан')


# однородный образец с учетом пористости (вода)
fig9, ax9 = plt.subplots()

# отрисовка температурных кривых
for i in range(5):
    plt.plot(x_lin1, l1.one_num(cond.a_w)[1800 * i],
             color=colors4[i], label=str(1800 * i / 60) + ' минут', linewidth=4)

# настройка подписей осей и пр.
f.plot_setup(r'$x, см$', r'$T, ^{o}С$',
             '', [0., 10.], [20., 26.], ax9, (1, 1))
f.text_on_plot(ax9, 3.2, 21.4, 'содержимое пор: вода')

plt.show()
