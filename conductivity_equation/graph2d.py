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

# однородный образец
fig1, ax1 = plt.subplots()

plt.figure(1)
plt.plot(x_lin1, l1.one_num(cond.a1)[0], color='#8B0000', label='0 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a1)[1800], color='#FF8C00', label='30 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a1)[3600], color='#DAA520', label='60 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a1)[5400], color='#228B22', label='90 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a1)[9000], color='#008080', label='150 минут', linewidth=4)
f.plot_setup(r'$x (см)$', r'$T (ºС)$',
             '', 10, ax1, (1, 1))

# двухслойный образец
fig2, ax2 = plt.subplots()

plt.figure(2)
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница \n известняк/глина', linewidth=4)
plt.plot(x_lin2, l2.T[0], color='#8B0000', label='0 минут', linewidth=4)
plt.plot(x_lin2, l2.T[1800], color='#FF8C00', label='30 минут', linewidth=4)
plt.plot(x_lin2, l2.T[3600], color='#DAA520', label='60 минут', linewidth=4)
plt.plot(x_lin2, l2.T[5400], color='#228B22', label='90 минут', linewidth=4)
plt.plot(x_lin2, l2.T[9000], color='#008080', label='150 минут', linewidth=4)
f.plot_setup(r'$x (см)$', r'$T (ºС)$',
             '', 20, ax2, (1.08, 1.05))
f.text_on_plot(ax2, 1.2, 23.67, 'известняк')
f.text_on_plot(ax2, 13.3, 24.67, 'глина')

# трехслойный образец
fig3, ax3 = plt.subplots()

plt.figure(3)
plt.axvline(x=10, color='#2F4F4F', ls='--', label='граница \n известняк/глина', linewidth=4)
plt.axvline(x=20, color='#BC8F8F', ls='--', label='граница \n глина/песок', linewidth=4)
plt.plot(x_lin3, l3.T[0], color='#8B0000', label='0 минут', linewidth=4)
plt.plot(x_lin3, l3.T[3000], color='#FF8C00', label='50 минут', linewidth=4)
plt.plot(x_lin3, l3.T[5400], color='#DAA520', label='90 минут', linewidth=4)
plt.plot(x_lin3, l3.T[7200], color='#228B22', label='120 минут', linewidth=4)
plt.plot(x_lin3, l3.T[9000], color='#008080', label='150 минут', linewidth=4)
f.plot_setup(r'$x (см)$', r'$T (ºС)$',
             '', 30, ax3, (1.15, 1.05))
f.text_on_plot(ax3, 0.8, 23.5, 'известняк')
f.text_on_plot(ax3, 13.5, 22.17, 'глина')
f.text_on_plot(ax3, 21, 21.25, 'сухой\nпесок')

# функциональная зависимость от глубины
fig4, ax4 = plt.subplots()

plt.figure(4)
plt.plot(x_lin1, vc.T[0], color='#8B0000', label='0 минут', linewidth=4)
plt.plot(x_lin1, vc.T[1500], color='#FF8C00', label='25 минут', linewidth=4)
plt.plot(x_lin1, vc.T[3000], color='#DAA520', label='50 минут', linewidth=4)
plt.plot(x_lin1, vc.T[4500], color='#228B22', label='75 минут', linewidth=4)
plt.plot(x_lin1, vc.T[6000], color='#008080', label='100 минут', linewidth=4)
f.plot_setup(r'$x (см)$', r'$T (ºС)$',
             '', 10, ax4, (1, 1))

# однородный образец с учетом пористости
fig5, ax5 = plt.subplots()

plt.figure(5)
plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[0], color='#8B0000', label='0 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[1800], color='#FF8C00', label='30 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[3600], color='#DAA520', label='60 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[5400], color='#228B22', label='90 минут', linewidth=4)
plt.plot(x_lin1, l1.one_num(cond.a_phi_air)[9000], color='#008080', label='150 минут', linewidth=4)
f.plot_setup(r'$x (см)$', r'$T (ºС)$',
             '', 10, ax5, (1, 1))

plt.show()
