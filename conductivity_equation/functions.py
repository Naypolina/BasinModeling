import matplotlib.pyplot as plt

def graph_setup(x_label, y_label, g_title, x_max):
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    plt.title(g_title, fontsize=16)
    plt.legend(fontsize=14, loc='upper right')
    plt.minorticks_on()
    plt.xlim([0., x_max])
    plt.ylim([20., 26.])
    plt.grid(which='major', color='#C0C0C0')
    plt.grid(which='minor', ls='--', color='#D3D3D3')