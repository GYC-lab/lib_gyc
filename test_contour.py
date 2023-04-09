from lib_gyc import *
import numpy as np
from matplotlib import pyplot as plt
import cmaps

n_points = 200
x_1d     = np.linspace(-4, 4, n_points)
y_1d     = np.linspace(-4, 4, n_points)
x_2d, y_2d = np.meshgrid(x_1d, y_1d)
z_2d = np.cos(x_2d)*np.cos(y_2d)

# ---------------------------- create a new Figure --------------------------- #
figname = 'my_contour'
figsize = (6,4.5)
plt.figure(figname,figsize=figsize)

# ------------------------------- plot contour ------------------------------- #
settings                    = gcontour_style()      # get default settings
settings["title"]           = '$u=\cos(x)\cos(y)$'  # add title
settings["xlabel"]          = '$x$'                 # add xlabel
settings["ylabel"]          = '$y$'                 # add ylabel
settings['yrotation']       = 0                     # change ytick rotation
settings["vmin"]            = -1                    # change min of colorbar
settings["vmax"]            = 1                     # change max of colorbar
settings["cmap"]            = cmaps.MPL_RdBu_r      # change colormap
settings["shading"]         = 'gouraud'             # change shading
settings["alpha"]           = 1                     # change alpha to make contour transparent
settings["show_colorbar"]   = True                  # show colorbar
settings["bar_label"]       = '$u$'                 # add colorbar label
settings["bar_tick_length"] = 12                    # change colorbar tick length
settings["bar_num_ticks"]   = 5                     # change colorbar number of ticks
gcontour(x_2d, y_2d, z_2d, settings)                # plot

# ----------------------------- plot contourline ----------------------------- #
settings               = gcontourline_style()   # get default settings
settings["levels"]     = [0]                    # change contour levels to set u=0
settings["linestyles"] = ['--']                 # change contour line style
settings["linewidths"] = [2]                    # change contour line width
settings["colors"]     = ['k']                  # change contour line color
gcontourline(x_2d, y_2d, z_2d,settings)          # plot

# --------------------------------- save fig --------------------------------- #
# default format is png, set _format='svg' or _format='pdf' to save as svg or pdf
gsavefig(figname)
plt.close(figname)