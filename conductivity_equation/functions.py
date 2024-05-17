import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def plot_setup(x_label, y_label, g_title, xlims, ylims, axis, majlocx, majlocy):
    plt.xlabel(x_label, fontsize=28, labelpad=15)
    plt.ylabel(y_label, fontsize=28, labelpad=15)
    plt.title(g_title, fontsize=28, fontweight='bold')
    plt.legend(fontsize=22, shadow=True, fancybox=True)
    plt.tight_layout()
    plt.tick_params(axis='both', which='major', labelsize=22, pad=8)
    plt.xlim(xlims)
    plt.ylim(ylims)
    plt.minorticks_on()
    axis.xaxis.set_major_locator(MultipleLocator(majlocx))
    axis.yaxis.set_major_locator(MultipleLocator(majlocy))
    axis.xaxis.set_minor_locator(AutoMinorLocator(2))
    axis.yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.grid(which='major', color='#C0C0C0', linewidth=2)
    plt.grid(which='minor', ls='--', color='#D3D3D3', linewidth=2)

def text_on_plot(axis, x_loc, y_loc, text):
    axis.text(x_loc, y_loc, text, fontsize=26, style='italic',
             bbox={'facecolor': '#C0C0C0', 'alpha': 0.4, 'pad': 5})

# цветовые палитры
colors1 = ['#8B0000', '#FF8C00', '#DAA520', '#228B22', '#008080']
colors2 = ['#cc254c', '#ab25cc', '#6525cc', '#2573cc', '#25a5cc']
colors3 = ['#d6432f', '#eb9413', '#dfe312', '#34b015', '#17bd96']
colors4 = ['#8715cf', '#1e33eb', '#1e7eeb', '#1ec5eb', '#21cc51']

