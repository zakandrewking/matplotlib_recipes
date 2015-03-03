import brewer2mpl
import math

def nrows_calc(count, ncols, rh=4, cw=4):
    """Return number of rows, number of columns, and figure size.

    Arguments
    ---------

    size: The number of axes to generate.

    ncols: The number of columns.

    rh: row height.

    cw: column width.
    
    """
    nrows = int(math.ceil(float(count)/ncols))
    figsize = (cw*ncols, rh*nrows)
    return nrows, ncols, figsize

def dark_qualitative_hex_colors(num=8):
    return brewer2mpl.get_map('Dark2', 'Qualitative', num).hex_colors

def blue_sequential_colors(num=9):
    return brewer2mpl.get_map('PuBu', 'Sequential', num)
