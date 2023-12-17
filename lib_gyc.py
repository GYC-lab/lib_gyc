'''
Author: GYC yuchen.ge@stu.pku.edu.cn
Date: 2023-03-05 17:50:23
LastEditTime: 2023-04-07 14:48:19
'''

# ---------------------------------------------------------------------------- #
#                                import library                                #
# ---------------------------------------------------------------------------- #
import numpy as np
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.colors as colors
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import LogLocator
from matplotlib.ticker import NullFormatter
# ---------------------------------------------------------------------------- #
#                                image settings                                #
# ---------------------------------------------------------------------------- #
mpl.rcParams['lines.linewidth']  = 2
mpl.rcParams['axes.linewidth']   = 1.5
mpl.rcParams['font.size']        = 20
mpl.rcParams['font.family']      = 'serif'
mpl.rcParams['font.serif']       = 'Times New Roman'
mpl.rcParams['mathtext.fontset'] = "stix"
mpl.rcParams['axes.prop_cycle']  = mpl.cycler(color=["#D20000", "#2d2dff",'#00D200',"k","#FF00FF"])

# ---------------------------------------------------------------------------- #
#                               section: plot                                  #
# ---------------------------------------------------------------------------- #
def assign_value(_var, _default):
    """
    This routine assigns the value of a variable if the variable is not defined
    """
    if _var == None:
        _var = _default
    return _var

def is_constant(arr, tol=1e-8):
    """
    This routine checks if an array is constant (avoid bugs when setting ticks)
    """
    return np.allclose(arr, arr[0], rtol=tol, atol=tol)

def gplot_style(fontsize=20,lineslinewidth=2,axeslinewidth=1.5):
    """
    This routine initializes the plot settings for gplot.
        - color: black
    """
    settings = {
        "line": {
            "color"          : 'k',
            "label"          : 'label of line',
            "width"          : lineslinewidth,
            "style"          : '-',
            "marker"         : '',
            "markerfacecolor": 'None',
            "markersize"     : 8,
            "markeredgewidth": 1,
            "markevery"      : 1,
            "zorder"         : 1,
            "clip_on"        : True,
        },
        "axis": {
            "xmin"            : None,
            "xmax"            : None,
            "ymin"            : None,
            "ymax"            : None,
            "x_scale"         : 'linear',
            "y_scale"         : 'linear',
            "equal_aspect"    : 'auto',
            "label_x_name"    : '$x$',
            "label_y_name"    : '$y$',
            "label_x_pad"     : 0,
            "label_y_pad"     : 16,
            "label_x_rotation": 0,
            "label_y_rotation": 0,
        },
        "tick": {
            "x_major_num"     : 5,
            "y_major_num"     : 5,
            "x_minor_num"     : 4,
            "y_minor_num"     : 4,
            "y_major_interval": None,
            "x_major_interval": None,
            "y_minor_interval": None,
            "x_minor_interval": None,
            "x_precision"     : 2,
            "y_precision"     : 2,
            "set_x_myticks"   : False,
            "set_y_myticks"   : False,
            "x_myticks"       : None,
            "y_myticks"       : None,
            "x_myticklabels"  : None,
            "y_myticklabels"  : None,
            "major_length"    : 8,
            "major_width"     : 1,
            "minor_length"    : 4,
            "minor_width"     : 1,
            "x_labelpad"      : 8,
            "y_labelpad"      : 8,
            "x_labelsize"     : fontsize,
            "y_labelsize"     : fontsize,
        },
        "leg": {
            "turn_on"   : True,
            "location"  : 'best',
            "fontsize"  : fontsize,
            "ncol"      : 1,
            "frameon"   : False,
            "framealpha": 1,
            "edgecolor" : 'k',
            "fancybox"  : False,
            "columnspacing": 1,
        },
        "title": {
            "name"           : 'my title',
            "fontsize"       : fontsize,
        },
        "grid": {
            "turn_on"         : False,
            "linecolor"       : 'k',
            "line_major_width": axeslinewidth,
            "line_minor_width": axeslinewidth,
            "linestyle"       : '--',
            "linealpha"       : 0.5,
        }
    }
    return settings

def gplot_style_r():
    """
    This routine initializes the plot settings for gplot.
        - color    : red #D20000
        - xlabel   : $x$
        - ylabel   : $y$
        - label    : ''
        - title    : ''
        - ylabelpad: 16
        - yrotation: 0
    """
    settings                          = gplot_style()
    settings["line_color"]            = '#D20000'
    settings["axis_label_x_name"]     = '$x$'
    settings["axis_label_y_name"]     = '$y$'
    settings["axis_label_y_pad"]      = 16
    settings["axis_label_y_rotation"] = 0
    
    return settings

def gplot_style_b():
    """
    This routine initializes the plot settings for gplot.
        - color    : blue
        - xlabel   : $x$
        - ylabel   : $y$
        - label    : ''
        - title    : ''
        - ylabelpad: 16
        - yrotation: 0
    """
    settings                          = gplot_style()
    settings["line_color"]            = '#2d2dff'
    settings["axis_label_x_name"]     = '$x$'
    settings["axis_label_y_name"]     = '$y$'
    settings["axis_label_y_pad"]      = 16
    settings["axis_label_y_rotation"] = 0
    
    return settings

def gplot_style_g():
    """
    This routine initializes the plot settings for gplot.
        - color    : green
        - xlabel   : $x$
        - ylabel   : $y$
        - label    : ''
        - title    : ''
        - ylabelpad: 16
        - yrotation: 0
    """
    settings              = gplot_style()
    settings["line_color"]            = '#00D200'
    settings["axis_label_x_name"]     = '$x$'
    settings["axis_label_y_name"]     = '$y$'
    settings["axis_label_y_pad"]      = 16
    settings["axis_label_y_rotation"] = 0
    
    return settings

def gcontour_style():
    """
    This routine initializes the plot settings for gcontour.
    """
    settings = {
        "pcolor_contourf"  : 0,
        "levels"           : 20,
        "alpha"            : 1.0,
        "cmap"             : 'jet',
        "xlabel"           : 'var 1',
        "ylabel"           : 'var 2',
        "title"            : 'my title',
        "shading"          : 'gouraud',
        "xlabelpad"        : 0,
        "xrotation"        : 0,
        "ylabelpad"        : 0,
        "yrotation"        : 90,
        "show_colorbar"    : False,
        "bar_num_ticks"    : 4,
        "bar_label"        : None,
        "bar_tick_length"  : 0.02,
        "bar_orientation"  : 'vertical',
        "bar_shrink"       : 1.0,
        "bar_position_size": [0.85,0.15,0.05,0.7],
        "bar_label_pad"    : [0,0],
        "antialiased"      : True,
        "show_grid"        : False,
        "linecolor"        : 'k',
        "linewidth"        : 1.0,
        "linestyle"        : '-',
        "equal_aspect"     : False,
        "xmin"             : None,
        "xmax"             : None,
        "ymin"             : None,
        "ymax"             : None,
        "vmin"             : None,
        "vmax"             : None,
        "xtick_major"      : None,
        "xtick_minor"      : None,
        "ytick_major"      : None,
        "ytick_minor"      : None,
    }
    return settings

def gcontourline_style():
    """
    This routine initializes the plot settings for gcontourline.
    """
    settings = {
        "levels"           : None,
        "linestyles"       : None,
        "linewidths"       : None,
        "colors"           : None
    }
    return settings

def gplot(x,y,gsettings=gplot_style()):
    """
    This routine plots the curve of a variable

    ---
    Parameters
    ---    
        - settings for a single line
            - [line][label]          : label of the line, which will be shown in the legend
            - [line][color]          : color of the line (choices: "k", "#D20000", "#2d2dff",'#00D200','#F97D01')
            - [line][style]          : style of the line (choices: "-", "--", "-.", ":")
            - [line][width]          : width of the line
            - [line][marker]         : marker of the line (choices: ["o", "s", "D", "v", "^", ">", "<")
            - [line][markerfacecolor]: set None to show hallow markers
            - [line][markersize]     : size of the markers
            - [line][markeredgewidth]: width of the marker edge
            - [line][markevery]      : set 1 to show all markers
            - [line][zorder]         : zorder of the line (the larger the value, the upper the line)
            - [line][clip_on]        : clip the line or not
        - settings for axis and x labels and y labels
            - [axis][xmin]            : range of x and y
            - [axis][xmax]            : range of x and y
            - [axis][ymin]            : range of x and y
            - [axis][ymax]            : range of x and y
            - [axis][x_scale]         : scale of the x axis (choices: ["linear", "log"])
            - [axis][y_scale]         : scale of the y axis (choices: ["linear", "log"])
            - [axis][equal_aspect]    : set equal aspect or not
            - [axis][label_x_name]    : x label, set $x$ to show x in latex
            - [axis][label_y_name]    : y label, set $y$ to show y in latex
            - [axis][label_x_pad]     : blank padding of the x label
            - [axis][label_y_pad]     : blank padding of the y label
            - [axis][label_x_rotation]: rotation of the x label
            - [axis][label_y_rotation]: rotation of the y label
        - settings for ticks
            - [tick][x_major_num]   : number of major ticks
            - [tick][y_major_num]   : number of major ticks
            - [tick][x_minor_num]   : number of minor ticks between two major ticks
            - [tick][y_minor_num]   : number of minor ticks between two major ticks
            - [tick][x_precision]   : precision of the tick labels
            - [tick][y_precision]   : precision of the tick labels
            - [tick][set_x_myticks] : set user-defined x ticks (can be uneven) or not
            - [tick][set_y_myticks] : set user-defined y ticks (can be uneven) or not
            - [tick][x_myticks]     : user-defined x ticks
            - [tick][y_myticks]     : user-defined y ticks
            - [tick][x_myticklabels]: user-defined x tick labels
            - [tick][y_myticklabels]: user-defined y tick labels
            - [tick][x_major_interval]: interval of major ticks of x
            - [tick][y_major_interval]: interval of major ticks of y
            - [tick][x_major_length]: length of x major ticks
            - [tick][y_major_length]: length of y major ticks
            - [tick][x_major_width] : width of x major ticks
            - [tick][y_major_width] : width of y major ticks
            - [tick][x_minor_length]: length of x minor ticks
            - [tick][y_minor_length]: length of y minor ticks
            - [tick][x_minor_width] : width of x minor ticks
            - [tick][y_minor_width] : width of y minor ticks
            - [tick][x_labelpad]    : pad of x tick labels
            - [tick][y_labelpad]    : pad of y tick labels
            - [tick][x_labelsize]   : fontsize of x tick labels
            - [tick][y_labelsize]   : fontsize of y tick labels
        - settings for legend
            - [leg][ncol]      : number of columns of the legend
            - [leg][fontsize]  : fontsize of the legend
            - [leg][location]  : location of the legend
            - [leg][frameon]   : show the frame of the legend or not
            - [leg][framealpha]: transparency of the frame of the legend
            - [leg][edgecolor] : color of the frame of the legend
            - [leg][fancybox]  : show the fancybox of the legend or not
        - settings for title
            - [title][name]    : title of the figure, which will be shown in the title
            - [title][fontsize]: fontsize of the title
        - settings for grids
            - [grid][on]       : show grid or not
            - [grid][linecolor]: color of the grid line
            - [grid][linewidth]: width of the grid line
            - [grid][linestyle]: style of the grid line
            - [grid][linealpha]    : transparency of the grid line
    ---
    Example
    ---
    settings          = gplot_style() # initialize the settings \n                                          
    settings["label"] = "label" # set the label                   \n                      
    settings["title"] = "title" # set the title                   \n                      
    gplot(x,y,settings) # plot the curve                          \n                  

    """

    # get the current figure and axis
    fig = plt.gcf()
    ax  = plt.gca()

    # parse the dictionary (sort randomly)
    _line_label            = gsettings["line"]["label"] # label of the line, which will be shown in the legend
    _line_color            = gsettings["line"]["color"] # color of the line  (choices: ["k", "#D20000", "#2d2dff",'#00D200','#F97D01'])
    _line_style            = gsettings["line"]["style"] # style of the line  (choices: ["-", "--", "-.", ":"])
    _line_width            = gsettings["line"]["width"] # width of the line
    _line_marker           = gsettings["line"]["marker"] # marker of the line (choices: ["o", "s", "D", "v", "^", ">", "<")
    _line_markersize       = gsettings["line"]["markersize"] # size of the marker
    _line_markerfacecolor  = gsettings["line"]["markerfacecolor"] # set None to show hallow markers
    _line_markevery        = gsettings["line"]["markevery"] # set None to show all markers
    _line_zorder           = gsettings["line"]["zorder"] # zorder of the line (the larger the value, the upper the line)
    _line_markeredgewidth  = gsettings["line"]["markeredgewidth"] # width of the marker edge
    _line_clip_on          = gsettings["line"]["clip_on"] # clip the line or not
    _axis_xmin             = gsettings["axis"]["xmin"] # range of x and y
    _axis_xmax             = gsettings["axis"]["xmax"] # range of x and y
    _axis_ymin             = gsettings["axis"]["ymin"] # range of x and y
    _axis_ymax             = gsettings["axis"]["ymax"] # range of x and y
    _axis_x_scale          = gsettings["axis"]["x_scale"] # scale of the x axis (choices: ["linear", "log"])
    _axis_y_scale          = gsettings["axis"]["y_scale"] # scale of the y axis (choices: ["linear", "log"])
    _axis_equal_aspect     = gsettings["axis"]["equal_aspect"] # set equal aspect or not
    _axis_label_x_name     = gsettings["axis"]["label_x_name"] # x label,    set $x$ to show x in latex
    _axis_label_y_name     = gsettings["axis"]["label_y_name"] # y label,    set $y$ to show y in latex
    _axis_label_x_pad      = gsettings["axis"]["label_x_pad"] # blank padding of the x label
    _axis_label_y_pad      = gsettings["axis"]["label_y_pad"] # blank padding of the y label
    _axis_label_x_rotation = gsettings["axis"]["label_x_rotation"] # rotation of the x label
    _axis_label_y_rotation = gsettings["axis"]["label_y_rotation"] # rotation of the y label
    _tick_x_major_interval = gsettings["tick"]["x_major_interval"] # interval of major ticks of x
    _tick_y_major_interval = gsettings["tick"]["y_major_interval"] # interval of major ticks of y
    _tick_x_minor_interval = gsettings["tick"]["x_minor_interval"] # interval of minor ticks of x
    _tick_y_minor_interval = gsettings["tick"]["y_minor_interval"] # interval of minor ticks of y
    _tick_x_major_num      = gsettings["tick"]["x_major_num"] # number of major ticks of x
    _tick_y_major_num      = gsettings["tick"]["y_major_num"] # number of major ticks of y
    _tick_x_minor_num      = gsettings["tick"]["x_minor_num"] # number of minor ticks of x
    _tick_y_minor_num      = gsettings["tick"]["y_minor_num"] # number of minor ticks of y
    _tick_x_precision      = gsettings["tick"]["x_precision"] # precision of the tick labels
    _tick_y_precision      = gsettings["tick"]["y_precision"] # precision of the tick labels
    _tick_set_x_myticks    = gsettings["tick"]["set_x_myticks"] # set user-defined x ticks (can be uneven) or not
    _tick_set_y_myticks    = gsettings["tick"]["set_y_myticks"] # set user-defined y ticks (can be uneven) or not
    _tick_x_myticks        = gsettings["tick"]["x_myticks"] # user-defined x ticks
    _tick_y_myticks        = gsettings["tick"]["y_myticks"] # user-defined y ticks
    _tick_x_myticklabels   = gsettings["tick"]["x_myticklabels"] # user-defined x tick labels
    _tick_y_myticklabels   = gsettings["tick"]["y_myticklabels"] # user-defined y tick labels
    _tick_major_length     = gsettings["tick"]["major_length"] # length of the major ticks
    _tick_major_width      = gsettings["tick"]["major_width"] # width of the major ticks
    _tick_minor_width      = gsettings["tick"]["minor_width"] # width of the minor ticks
    _tick_minor_length     = gsettings["tick"]["minor_length"] # length of the minor ticks
    _tick_x_labelpad       = gsettings["tick"]["x_labelpad"] # padding of the x tick labels
    _tick_y_labelpad       = gsettings["tick"]["y_labelpad"] # padding of the y tick labels
    _leg_on                = gsettings["leg"]["turn_on"] # show legend or not
    _leg_location          = gsettings["leg"]["location"] # location of the legend
    _leg_fontsize          = gsettings["leg"]["fontsize"] # fontsize of the legend
    _leg_ncol              = gsettings["leg"]["ncol"] # number of columns of the legend
    _leg_frameon           = gsettings["leg"]["frameon"] # show legend frame or not
    _leg_framealpha        = gsettings["leg"]["framealpha"] # alpha of the legend frame
    _leg_edgecolor         = gsettings["leg"]["edgecolor"] # edgecolor of the legend frame
    _leg_fancybox          = gsettings["leg"]["fancybox"] # show fancybox or not
    _leg_columnspacing     = gsettings["leg"]["columnspacing"] # spacing between columns
    _title_name            = gsettings["title"]["name"] # title of the plot
    _title_fontsize        = gsettings["title"]["fontsize"] # fontsize of the title
    _grid_on               = gsettings["grid"]["turn_on"] # show grid or not
    _grid_linestyle        = gsettings["grid"]["linestyle"] # linestyle of the grid
    _grid_line_major_width = gsettings["grid"]["line_major_width"] # width of the major grid
    _grid_line_minor_width = gsettings["grid"]["line_minor_width"] # width of the minor grid
    _grid_linealpha        = gsettings["grid"]["linealpha"] # alpha of the grid
    _grid_linecolor        = gsettings["grid"]["linecolor"] # linecolor of the grid

    _axis_xmin             = assign_value(_axis_xmin, np.min(x))
    _axis_xmax             = assign_value(_axis_xmax, np.max(x))
    _axis_ymin             = assign_value(_axis_ymin, np.min(y))
    _axis_ymax             = assign_value(_axis_ymax, np.max(y))

    # num_line = len(x)

    # plot line
    # for i in range(num_line):
    ax.plot(x,y, label = _line_label, color= _line_color, linestyle = _line_style, linewidth = _line_width,\
            marker = _line_marker, markersize = _line_markersize, markerfacecolor = _line_markerfacecolor, markevery= _line_markevery,\
            markeredgewidth=_line_markeredgewidth,zorder = _line_zorder)
                
    # ------------- title ------------------
    ax.set_title(_title_name, fontsize=_title_fontsize)

    # ------------- axis ------------------
    ax.set_xlim  (_axis_xmin, _axis_xmax)
    ax.set_ylim  (_axis_ymin, _axis_ymax)
    ax.set_xlabel(_axis_label_x_name, labelpad=_axis_label_x_pad, rotation=_axis_label_x_rotation)
    ax.set_ylabel(_axis_label_y_name, labelpad=_axis_label_y_pad, rotation=_axis_label_y_rotation)
    ax.set_aspect(_axis_equal_aspect, adjustable='box')

    if _axis_x_scale != "log" and _axis_y_scale != "log":
        # set ticks based on the data for linear scale
        if (is_constant(x) or is_constant(y)) and (_axis_xmin == _axis_xmax or _axis_ymin == _axis_ymax):
            print("(lib_gyc) Warning: x or y is constant. ['axis']['xmin'] and ['axis']['xmax'] should be set manually.")
            
        _tick_x_major_interval = assign_value(_tick_x_major_interval, (_axis_xmax-_axis_xmin)/(_tick_x_major_num-1))
        _tick_x_minor_interval = assign_value(_tick_x_minor_interval, (_axis_xmax-_axis_xmin)/(_tick_x_major_num-1)/(_tick_x_minor_num+1))
        _tick_y_major_interval = assign_value(_tick_y_major_interval, (_axis_ymax-_axis_ymin)/(_tick_y_major_num-1))
        _tick_y_minor_interval = assign_value(_tick_y_minor_interval, (_axis_ymax-_axis_ymin)/(_tick_y_major_num-1)/(_tick_y_minor_num+1))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(_tick_x_major_interval))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(_tick_x_minor_interval))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(_tick_y_major_interval)) 
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(_tick_y_minor_interval))
        format_decimal_x(precision=_tick_x_precision)
        format_decimal_y(precision=_tick_y_precision)

    elif _axis_x_scale == "log" and _axis_y_scale == "log":
        print("lib_gyc: using log scale, make sure xmin or ymin does not start from zero.")
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0))
        ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=(2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)))
        ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)))
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.yaxis.set_minor_formatter(NullFormatter())
    elif _axis_x_scale == "log" and _axis_y_scale != "log":
        print("lib_gyc: using log scale, make sure xmin does not start from zero.")
        ax.set_xscale('log')
        ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0))
        ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=(2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)))
        ax.xaxis.set_minor_formatter(NullFormatter())
    elif _axis_x_scale != "log" and _axis_y_scale == "log":
        print("lib_gyc: using log scale, make sure ymin does not start from zero.")
        ax.set_yscale('log')
        ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)))
        ax.yaxis.set_minor_formatter(NullFormatter())

    # set ticks based on the user-defined ticks
    if _tick_set_x_myticks:
        # check validity
        ax.set_xticks([])
        if _tick_x_myticks == None or _tick_x_myticks == []:
            print("lib_gyc: Key 'myxticks' is empty! Remove the x ticks.")
        else:
            if _tick_x_myticklabels == None or _tick_x_myticklabels == []:
                print("lib_gyc: Key 'myxticklabels' is empty! Set 'myxticklabels' based on the 'myxticks'.")
                _tick_x_myticklabels = []
                for i in range(len(_tick_x_myticks)):
                    _tick_x_myticklabels.append(str(_tick_x_myticks[i]))
            elif len(_tick_x_myticks) != len(_tick_x_myticklabels):
                print("lib_gyc: The length of 'myxticks' and 'myticklabels' are not equal! Set 'myxticklabels' based on the 'myxticks'.")
                _tick_x_myticklabels = []
                for i in range(len(_tick_x_myticks)):
                    _tick_x_myticklabels.append(str(_tick_x_myticks[i]))
            # set ticks
            ax.set_xticks(_tick_x_myticks, _tick_x_myticklabels)

    # set ticks based on the user-defined ticks
    if _tick_set_y_myticks:
        # check validity
        ax.set_yticks([])
        if _tick_y_myticks == None or _tick_y_myticks == []:
            print("lib_gyc: Key 'myyticks' is empty! Remove the y ticks.")
        else:
            if _tick_y_myticklabels == None or _tick_y_myticklabels == []:
                print("lib_gyc: Key 'myyticklabels' is empty! Set 'myyticklabels' based on the 'myyticks'.")
                _tick_y_myticklabels = []
                for i in range(len(_tick_y_myticks)):
                    _tick_y_myticklabels.append(str(_tick_y_myticks[i]))
            elif len(_tick_y_myticks) != len(_tick_y_myticklabels):
                print("lib_gyc: The length of 'myyticks' and 'myticklabels' are not equal! Set 'myyticklabels' based on the 'myyticks'.")
                _tick_y_myticklabels = []
                for i in range(len(_tick_y_myticks)):
                    _tick_y_myticklabels.append(str(_tick_y_myticks[i]))
            ax.set_yticks(_tick_y_myticks, _tick_y_myticklabels)

    # set tick parameters
    ax.tick_params(direction='in',which='both')
    ax.tick_params(axis='both', which='major', length=_tick_major_length, width = _tick_major_width)
    ax.tick_params(axis='both', which='minor', length=_tick_minor_length, width = _tick_minor_width)
    ax.tick_params(axis='x', pad=_tick_x_labelpad)
    ax.tick_params(axis='y', pad=_tick_y_labelpad)

    # ------------- legend ------------------
    if _leg_on:
        ax.legend(loc=_leg_location,fontsize=_leg_fontsize,ncol=_leg_ncol, frameon=_leg_frameon, \
                  edgecolor=_leg_edgecolor, framealpha=_leg_framealpha, fancybox=_leg_fancybox,\
                  columnspacing=_leg_columnspacing)

    # ------------- grid ------------------
    if _grid_on:
        ax.grid(which='major',axis='both',linewidth=_grid_line_major_width,color=_grid_linecolor,\
            linestyle=_grid_linestyle,alpha=_grid_linealpha)
        ax.grid(which='minor',axis='both',linewidth=_grid_line_minor_width,color=_grid_linecolor,\
            linestyle=_grid_linestyle,alpha=_grid_linealpha)        

def format_decimal_x(precision=2):
    """
    This routine formats the origin of the plot
    """ 
    def tick_formatter(x, pos):
        if x == 0.0:
            return '0'
        else:
            return '{:.{}f}'.format(x,precision)
            
            # return '{:.2f}'.format(x)
    ax = plt.gca()

    ax.xaxis.set_major_formatter(FuncFormatter(tick_formatter))

def format_decimal_y(precision=2):
    """
    This routine formats the origin of the plot
    """ 
    def tick_formatter(x, pos):
        if x == 0.0:
            return '0'
        else:
            return '{:.{}f}'.format(x,precision)
            
            # return '{:.2f}'.format(x)
    ax = plt.gca()

    ax.yaxis.set_major_formatter(FuncFormatter(tick_formatter))

def gcontour(x,y,var,gsettings=gcontour_style()):
    """
    This routine plots the contour of a variable
            
    ---
    Parameters
    ---    
        - settings for contourf 
            - pcolor_contourf: plot pcolormesh(default) or contourf(use 1 to activate)
            - levels: levels of the contourf
        - settings for axis
            - xmin, xmax, ymin, ymax: range of x and y
            - equal_aspect: equal aspect or not
        - settings for color
            - vmin: minimum value mapped to color
            - vmax: maximum value mapped to color
            - cmap: colormap
            - alpha: alpha of the contour
            - shading: shading of the contour
            - antialiasing: anti-aliasing or not
        - settings for x label and y label
            - xlabel: x label: set $x$ to show x in latex
            - ylabel: y label: set $y$ to show y in latex
            - xlabelpad: labelpad of x label
            - ylabelpad: labelpad of y label
            - xrotation: angle of x label
            - yrotation: angle of y label
        - settings for title
            - title: title of the contour
        - settings for ticks    
            - xtick_major: major x ticks
            - xtick_minor: minor x ticks
            - ytick_major: major y ticks
            - ytick_minor: minor y ticks
        - settings for colorbar
            - show_colorbar: show colorbar or not
            - bar_num_ticks: number of ticks in the colorbar
            - bar_label: label of the colorbar
            - bar_tick_length: length of the ticks in the colorbar
            - bar_tick_width: width of the ticks in the colorbar
            - bar_orientation: orientation of the colorbar
            - bar_shrink: shrink of the colorbar
            - bar_position: position of the colorbar
            - bar_labelpad: labelpad of the colorbar
        - settings for grid
            - show_grid: show grid or not
            - linecolor: color of the grid
            - linewidth: width of the grid
            - linestyle: style of the grid
        ---
        Example
        ---
        settings          = gcontour_style()      # get default settings \n               
        settings["title"] = '$u=\cos(x)\cos(y)$'  # add title            \n   
        gcontour(x_2d, y_2d, z_2d, settings)      # plot the curve       \n   
    """

    # get the current figure and axis
    fig = plt.gcf()
    ax  = plt.gca()

    # parse the dictionary
    _pcolor_contourf   = gsettings["pcolor_contourf"]   # use pcolor or contourf
    _levels            = gsettings["levels"]            # levels of the contourf
    _alpha             = gsettings["alpha"]             # alpha of the contour
    _xmin              = gsettings["xmin"]              # range of x
    _xmax              = gsettings["xmax"]              # range of x
    _ymin              = gsettings["ymin"]              # range of y
    _ymax              = gsettings["ymax"]              # range of y
    _cmap              = gsettings["cmap"]              # colormap
    _shading           = gsettings["shading"]           # shading of the contour
    _title             = gsettings["title"]             # title of the line, which will be shown in the top of the figure
    _xlabel            = gsettings["xlabel"]            # x label: set $x$ to show x in latex
    _ylabel            = gsettings["ylabel"]            # y label: set $y$ to show y in latex
    _xlabelpad         = gsettings["xlabelpad"]         # labelpad of x label
    _ylabelpad         = gsettings["ylabelpad"]         # labelpad of y label
    _xrotation         = gsettings["xrotation"]         # angle of x label
    _yrotation         = gsettings["yrotation"]         # angle of y label
    _xtick_major       = gsettings["xtick_major"]       # x major tick interval
    _xtick_minor       = gsettings["xtick_minor"]       # x minor tick interval
    _ytick_major       = gsettings["ytick_major"]       # y major tick interval
    _ytick_minor       = gsettings["ytick_minor"]       # y minor tick interval
    _vmax              = gsettings["vmax"]              # max value of the colorbar
    _vmin              = gsettings["vmin"]              # min value of the colorbar
    _show_colorbar     = gsettings["show_colorbar"]     # show colorbar or not
    _bar_num_ticks     = gsettings["bar_num_ticks"]     # number of ticks in the colorbar
    _bar_label         = gsettings["bar_label"]         # label of the colorbar
    _bar_tick_length   = gsettings["bar_tick_length"]   # length of the colorbar ticks
    _bar_orientation   = gsettings["bar_orientation"]   # orientation of the colorbar
    _bar_shrink        = gsettings["bar_shrink"]        # shrink the colorbar
    _bar_position_size = gsettings["bar_position_size"] # position and size of the colorbar
    _bar_label_pad     = gsettings["bar_label_pad"]     # position of the colorbar label
    _antialiased       = gsettings["antialiased"]       # antialiased
    _show_grid         = gsettings["show_grid"]         # show grid
    _linecolor         = gsettings["linecolor"]         # edgecolor
    _linewidth         = gsettings["linewidth"]         # linewidth
    _linestyle         = gsettings["linestyle"]         # linestyle
    _equal_aspect      = gsettings["equal_aspect"]      # equal aspect

    # assign default values
    _xmin              = assign_value(_xmin, np.min(x))
    _xmax              = assign_value(_xmax, np.max(x))
    _ymin              = assign_value(_ymin, np.min(y))
    _ymax              = assign_value(_ymax, np.max(y))
    _xtick_major       = assign_value(_xtick_major, (np.max(x)-np.min(x))/4) # 5 major xticks
    _xtick_minor       = assign_value(_xtick_minor, (np.max(x)-np.min(x))/16) # 4 minor xtick between 2 major xticks
    _ytick_major       = assign_value(_ytick_major, (np.max(y)-np.min(y))/4) # 5 major yticks
    _ytick_minor       = assign_value(_ytick_minor, (np.max(y)-np.min(y))/16) # 4 minor ytick between 2 major yticks
    _vmax              = assign_value(_vmax, np.max(var))
    _vmin              = assign_value(_vmin, np.min(var))
    
    # plot the contour
    if _pcolor_contourf == 1:
        pcm = plt.contourf(x, y, var,levels=_levels,cmap=_cmap,vmax=_vmax,vmin=_vmin,antialiased=_antialiased,alpha=_alpha)
    else:
        pcm = plt.pcolormesh(x, y, var, cmap=_cmap,shading=_shading,vmax=_vmax,vmin=_vmin,\
                        antialiased=_antialiased,linewidth=_linewidth,alpha=_alpha)

    pcm.set_clim(_vmin, _vmax)
    
    # ------------- label ------------------
    plt.xlabel(_xlabel,labelpad=_xlabelpad,rotation=_xrotation)
    plt.ylabel(_ylabel,labelpad=_ylabelpad,rotation=_yrotation)
    plt.title(_title)

    plt.xlabel(_xlabel)
    plt.ylabel(_ylabel)

    # ------------- range ------------------
    plt.xlim([_xmin,_xmax])
    plt.ylim([_ymin,_ymax])

    # ------------- ticks -------------x-----
    plt.tick_params(direction='in',which='both')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(_xtick_major)) 
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(_xtick_minor))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(_ytick_major)) 
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(_ytick_minor))

    if _equal_aspect:
        ax.set_aspect(_equal_aspect, adjustable='box')

    # ------------- colorbar ------------------
    if _show_colorbar:
        cbar = plt.colorbar(orientation=_bar_orientation,shrink=_bar_shrink)
        cbar.set_label(_bar_label)
        cbar.ax.tick_params(direction='in',length=_bar_tick_length)
        cbar.ax.set_position(_bar_position_size)
        cbar.set_ticks(np.linspace(_vmin,_vmax,_bar_num_ticks)) 

    # ------------- grid ------------------
    if _show_grid:
        plt.grid(which='major',axis='both',linewidth=_linewidth,color=_linecolor,linestyle=_linestyle)
        plt.grid(which='minor',axis='both',linewidth=_linewidth,color=_linecolor,linestyle=_linestyle)        

def gcontourline(x,y,var,gsettings=gcontourline_style()):
    """
    contour line
        -  levels     : contour levels
        -  colors     : contour colors
        -  linewidths : contour linewidths
        -  linestyles : contour linestyles
    """
    _levels     = gsettings['levels']
    _colors     = gsettings['colors']
    _linewidths = gsettings['linewidths']
    _linestyles = gsettings['linestyles']

    _levels     = assign_value(_levels, 0)
    _colors     = assign_value(_colors, 'k')
    _linewidths = assign_value(_linewidths, 1.0)
    _linestyles = assign_value(_linestyles, 'solid')

    plt.contour(x,y,var,levels=_levels,colors=_colors,\
                linewidths=_linewidths,linestyles=_linestyles)

def gsavefig(_filename,_figsize=None,_dpi=300,_format='png'):
    """
    This routine is used to save figure
    """
    if _figsize is None:
        _figsize = plt.gcf().get_size_inches()
    else:
        plt.gcf().set_size_inches(_figsize[0],_figsize[1])

    _filename_all = _filename + '.' + _format

    # plt.savefig(fname=_filename_all,format=_format,dpi=_dpi,bbox_inches='tight',pad_inches=0.1)
    plt.savefig(fname=_filename_all,format=_format,dpi=_dpi,pad_inches=0.1)