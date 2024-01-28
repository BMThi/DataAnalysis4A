# draw a vector frome x0 to x1
# in dim 2

def draw_vector(x0, x1, ax=None):
    ax = ax or plt.gca()
    arrowprops = dict(arrowstyle = '->', 
                      linewidth = 2, 
                      shrinkA = 0, 
                      shrinkB = 0)
    ax.annotate('', x1, x0, arrowprops=arrowprops)