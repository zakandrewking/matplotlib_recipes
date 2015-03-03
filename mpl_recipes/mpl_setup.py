import matplotlib as mpl
import IPython
from IPython.core.magic import register_line_magic

@register_line_magic
def mpl_setup(line):
    IPython.get_ipython().magic('pylab --no-import-all inline')

    try:
        import seaborn as sns
        sns.set(style="darkgrid")
    except ImportError:
        from warnings import warn
        warn('Seaborn not installed')

    mpl.rcParams['font.sans-serif'] = 'Helvetica Neue, Helvetica, Avant Garde, Computer Modern Sans serif'
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['savefig.bbox'] = 'tight'
    mpl.rcParams['savefig.pad_inches'] = 0
    mpl.rcParams['text.usetex'] = False
    mpl.rcParams['lines.linewidth'] = 3
    mpl.rcParams['font.size'] = 15
    mpl.rcParams['axes.labelsize'] = 17
    mpl.rcParams['axes.titlesize'] = 17
    mpl.rcParams['xtick.labelsize'] = 15
    mpl.rcParams['ytick.labelsize'] = 15
    mpl.rcParams['legend.fontsize'] = 17
