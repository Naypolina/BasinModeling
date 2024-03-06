import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def plot_setup(x_label, y_label, g_title, xlims, ylims, axis, bbox):
    plt.xlabel(x_label, fontsize=26)
    plt.ylabel(y_label, fontsize=26)
    plt.title(g_title, fontsize=24, fontweight='bold')
    plt.legend(fontsize=18, bbox_to_anchor=bbox, loc='upper right',
               shadow=True, fancybox=True)
    plt.tight_layout()
    plt.tick_params(axis='both', which='major', labelsize=20)
    plt.xlim(xlims)
    plt.ylim(ylims)
    plt.minorticks_on()
    axis.xaxis.set_minor_locator(AutoMinorLocator(2))
    axis.yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.grid(which='major', color='#C0C0C0', linewidth=2)
    plt.grid(which='minor', ls='--', color='#D3D3D3', linewidth=2)

def text_on_plot(axis, x_loc, y_loc, text):
    axis.text(x_loc, y_loc, text, fontsize=26, style='italic',
             bbox={'facecolor': '#C0C0C0', 'alpha': 0.35, 'pad': 5})

