from lib_gyc import *
import numpy as np
from matplotlib import pyplot as plt

# ------------------------------- generate data ------------------------------ #
x   = np.linspace(0, 1, 100)
y_1 = x**(1/2)
y_2 = x**(1/3)
y_3 = x**(1/4)
y_4 = x**(1/5)

# ---------------------------- create a new Figure --------------------------- #
figname = 'my_plot'
figsize = (6,4.5)
plt.figure(figname,figsize=figsize)

# -------------------------------- first curve ------------------------------- #
settings          = gplot_style_k()         # get default settings
settings["label"] = '$y=x^{1/2}$'           # add label
gplot(x,y_1,settings)                       # plot

# ------------------------------- second curve ------------------------------- #
settings              = gplot_style_r()     # get default settings
settings["label"]     = '$y=x^{1/3}$'       # add label
settings["marker"]    = 'D'                 # add marker
settings["markevery"] = 10                  # change marker frequency
gplot(x,y_2,settings)

# -------------------------------- third curve ------------------------------- #
settings              = gplot_style_b()     # get default settings
settings["label"]     = '$y=x^{1/4}$'       # add label
settings["marker"]    = '+'                 # add marker
settings["markevery"] = 10                  # change marker frequency
settings["linestyle"] = '-.'                # change linestyle
gplot(x,y_3,settings)

# ------------------------------- fourth curve ------------------------------- #
settings                = gplot_style_g()   # get default settings
settings["label"]       = '$y=x^{1/5}$'     # add label
settings["marker"]      = 'x'               # add marker
settings["markevery"]   = 10                # change marker frequency
settings["linestyle"]   = ':'               # change linestyle

# final settings (works for all curves)
settings["xmin"]        = 1e-6              # change min of x
settings["xmax"]        = 1                 # change max of x
settings["legfontsize"] = 20                # change legend fontsize
settings["legloc"]      = 'lower right'     # change legend location
gplot(x,y_4,settings)

# --------------------------------- save fig --------------------------------- #
# default format is png, set _format='svg' or _format='pdf' to save as svg or pdf
gsavefig(figname)
plt.close(figname)