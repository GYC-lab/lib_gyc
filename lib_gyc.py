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

# ---------------------------------------------------------------------------- #
#                                image settings                                #
# ---------------------------------------------------------------------------- #
mpl.rcParams['lines.linewidth']  = 2
mpl.rcParams['axes.linewidth']   = 1.5
mpl.rcParams['font.size']        = 22
mpl.rcParams['font.family']      = 'serif'
mpl.rcParams['font.serif']       = 'Times New Roman'
mpl.rcParams['mathtext.fontset'] = "stix"
mpl.rcParams['axes.prop_cycle']  = mpl.cycler(color=["#D20000", "2d2dff",'#00D200',"k","#FF00FF"])

# ---------------------------------------------------------------------------- #
#                               section: general                               #
# ---------------------------------------------------------------------------- #
def assign_value(_var, _default):
    """
    This routine assigns the value of a variable if the variable is not defined
    """
    if _var == None:
        _var = _default
    return _var

def gplot_style_k():
    """
    This routine initializes the plot settings for gplot.
        - color: black
    """
    settings = {
        "color"          : 'k',
        "linewidth"      : 2,
        "linestyle"      : '-',
        "marker"         : 'None',
        "markersize"     : 8,
        "markerfacecolor": 'None',
        "xlabel"         : '$x$',
        "ylabel"         : '$y$',
        "label"          : 'line 1',
        "title"          : 'my title',
        "leg_loc"        : 'best',
        "xlabelpad"      : 0,
        "xrotation"      : 0,
        "ylabelpad"      : 0,
        "yrotation"      : 90,
        "markevery"      : 1,
        "show_grid"      : False,
        "gridlinecolor"  : None,
        "gridlinewidth"  : 0.0,
        "gridlinestyle"  : None,
        "xscale"         : 'linear',
        "yscale"         : 'linear',
        "equal_aspect"   : False,
        "zorder"         : 3,
        "titlefontsize"  : 22,
        "legfontsize"    : 22,
        "clip_on"        : True,
        "leg_ncol"       : 1,
        "xmin"           : None,
        "xmax"           : None,
        "ymin"           : None,
        "ymax"           : None,
        "xtick_major"    : None,
        "xtick_minor"    : None,
        "ytick_major"    : None,
        "ytick_minor"    : None,
        "show_legend"    : True,
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
    settings              = gplot_style_k()
    settings["color"]     = '#D20000'
    settings["xlabel"]    = '$x$'
    settings["ylabel"]    = '$y$'
    settings["ylabelpad"] = 16
    settings["yrotation"] = 0
    
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
    settings              = gplot_style_k()
    settings["color"]     = '#2d2dff'
    settings["xlabel"]    = '$x$'
    settings["ylabel"]    = '$y$'
    settings["ylabelpad"] = 16
    settings["yrotation"] = 0
    
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
    settings              = gplot_style_k()
    settings["color"]     = '#00D200'
    settings["xlabel"]    = '$x$'
    settings["ylabel"]    = '$y$'
    settings["ylabelpad"] = 16
    settings["yrotation"] = 0
    
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

def gaxzoom_style():
    """
    This routine initializes the plot settings for gaxzoom.
    """
    settings = {
        "posi_size"      : None,
        "xmin"           : None,
        "xmax"           : None,
        "ymin"           : None,
        "ymax"           : None,
        "linecolor"      : None,
        "linewidth"      : None,
        "linestyle"      : None,
        "xticklabel"     : None,
        "yticklabel"     : None,
        "equal_aspect"   : None,
        "labelsize"      : None,
        "marker"         : None,
        "markersize"     : None,
        "markevery"      : None,
        "markerfacecolor": None,
    }
    return settings

def gplot(x,y,gsettings=gplot_style_k()):
    """
    This routine plots the curve of a variable

    ---
    Example
    ---
    settings          = gplot_style_k() # initialize the settings \n                                          
    settings["label"] = "label" # set the label                   \n                      
    settings["title"] = "title" # set the title                   \n                      
    gplot(x,y,settings) # plot the curve                          \n                  
    ---
    Parameters
    ---    
        - settings for curves
            - color          : color of the curve (choices: "k", "#D20000", "#2d2dff",'#00D200','#F97D01')
            - linestyle      : style of the curve (choices: "-", "--", "-.", ":")
            - label          : label of the curve, which will be shown in the legend
            - zorder         : zorder of the curve (the larger the value, the upper the curve)
            - clip_on        : clip the curves or not
        - settings for title
            - title          : title of the figure, which will be shown in the title
            - titlefontsize  : fontsize of the title
        - settings for markers
            - marker         : marker of the curve (choices: ["o", "s", "D", "v", "^", ">", "<")
            - markerfacecolor: set None to show hallow markers
        - settings for ticks
            - xtick_major    : major ticks of x
            - xtick_minor    : minor ticks of x
            - ytick_major    : major ticks of y
            - ytick_minor    : minor ticks of y
        - settings for x labels and y labels
            - xlabel         : x label          : set $x$ to show x in latex
            - ylabel         : y label          : set $y$ to show y in latex
            - xlabelpad      : blank padding of the x label
            - ylabelpad      : blank padding of the y label
            - xrotation      : rotation of the x label
            - yrotation      : rotation of the y label
        - settings for grids
            - show_grid      : show grid or not
            - gridlinecolor  : color of the grid line
            - gridlinewidth  : width of the grid line
            - gridlinestyle  : style of the grid line
        - settings for axis
            - xmin,xmax,ymin,ymax: range of x and y
            - xscale         : scale of the x axis (choices: ["linear", "log"])
            - yscale         : scale of the y axis (choices: ["linear", "log"])
            - equal_aspect   : set equal aspect or not
        - settings for legend
            - leg_loc        : location of the legend
            - legfontsize    : fontsize of the legend
            - leg_ncol       : number of columns of the legend
    """

    # get the current figure and axis
    fig = plt.gcf()
    ax  = plt.gca()

    # parse the dictionary
    _color           = gsettings["color"]            # color of the line  (choices: ["k", "#D20000", "#2d2dff",'#00D200','#F97D01'])
    _linestyle       = gsettings["linestyle"]        # style of the line  (choices: ["-", "--", "-.", ":"])
    _linewidth       = gsettings["linewidth"]        # width of the line
    _marker          = gsettings["marker"]           # marker of the line (choices: ["o", "s", "D", "v", "^", ">", "<")
    _markersize      = gsettings["markersize"]       # size of the marker
    _markerfacecolor = gsettings["markerfacecolor"]  # set None to show hallow markers
    _xlabel          = gsettings["xlabel"]           # x label: set $x$ to show x in latex
    _ylabel          = gsettings["ylabel"]           # y label: set $y$ to show y in latex
    _label           = gsettings["label"]            # label of the line, which will be shown in the legend
    _title           = gsettings["title"]            # title of the line, which will be shown in the top of the figure
    _xmin            = gsettings["xmin"]             # range of x: xmin
    _xmax            = gsettings["xmax"]             # range of x: xmax
    _ymin            = gsettings["ymin"]             # range of y: ymin
    _ymax            = gsettings["ymax"]             # range of y: ymax
    _xtick_major     = gsettings["xtick_major"]      # x major tick interval
    _xtick_minor     = gsettings["xtick_minor"]      # x minor tick interval
    _ytick_major     = gsettings["ytick_major"]      # y major tick interval
    _ytick_minor     = gsettings["ytick_minor"]      # y minor tick interval
    _leg_loc         = gsettings["leg_loc"]          # location of the legend (choices: ["best", "upper right", "upper left", "lower left", "lower right", "right", "center left", "center right", "lower center", "upper center", "center"])
    _xlabelpad       = gsettings["xlabelpad"]        # labelpad of x label
    _ylabelpad       = gsettings["ylabelpad"]        # labelpad of y label
    _xrotation       = gsettings["xrotation"]        # angle of x label
    _yrotation       = gsettings["yrotation"]        # angle of y label
    _markevery       = gsettings["markevery"]        # show markers every '_markevery' points
    _show_grid       = gsettings["show_grid"]        # show grid
    _gridlinecolor   = gsettings["gridlinecolor"]    # line color of grid
    _gridlinewidth   = gsettings["gridlinewidth"]    # line width of grid
    _gridlinestyle   = gsettings["gridlinestyle"]    # line style of grid
    _xscale          = gsettings["xscale"]           # scale of x axis (choices: ["linear", "log", "symlog", "logit"])
    _yscale          = gsettings["yscale"]           # scale of y axis (choices: ["linear", "log", "symlog", "logit"])
    _equal_aspect    = gsettings["equal_aspect"]     # set equal aspect or not
    _zorder          = gsettings["zorder"]           # zorder of the line
    _titlefontsize   = gsettings["titlefontsize"]    # fontsize of the title
    _legfontsize     = gsettings["legfontsize"]      # fontsize of the legend
    _clip_on         = gsettings["clip_on"]          # clip the line or not
    _show_legend     = gsettings["show_legend"]      # show legend or not
    _leg_ncol        = gsettings["leg_ncol"]         # number of columns in the legend

    # assign default values
    _xmin            = assign_value(_xmin, np.min(x))
    _xmax            = assign_value(_xmax, np.max(x))
    _ymin            = assign_value(_ymin, np.min(y))
    _ymax            = assign_value(_ymax, np.max(y))
    _xtick_major     = assign_value(_xtick_major, (np.max(x)-np.min(x))/4) # 5 major xticks
    _xtick_minor     = assign_value(_xtick_minor, (np.max(x)-np.min(x))/8) # 1 minor xtick between 2 major xticks
    _ytick_major     = assign_value(_ytick_major, (np.max(y)-np.min(y))/4) # 5 major yticks
    _ytick_minor     = assign_value(_ytick_minor, (np.max(y)-np.min(y))/8) # 1 minor ytick between 2 major yticks

    # plot the contour
    plt.plot(x, y,color=_color,label=_label,linestyle=_linestyle, linewidth=_linewidth, zorder = _zorder, clip_on=_clip_on\
             ,marker=_marker, markersize=_markersize, markerfacecolor=_markerfacecolor, markevery=_markevery)
    
    # ------------- label ------------------
    plt.xlabel(_xlabel,labelpad=_xlabelpad,rotation=_xrotation)
    plt.ylabel(_ylabel,labelpad=_ylabelpad,rotation=_yrotation)
    plt.title(_title,fontsize=_titlefontsize)

    # ------------- range ------------------
    plt.xlim([_xmin,_xmax])
    plt.ylim([_ymin,_ymax])

    # ------------- scale -------------------
    if _xscale == 'log':
        plt.xscale('log')
    if _yscale == 'log':
        plt.yscale('log')

    # ------------- ticks ------------------
    plt.tick_params(direction='in',which='both')
    ax=plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(_xtick_major)) 
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(_xtick_minor))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(_ytick_major)) 
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(_ytick_minor))
    if _equal_aspect:
        ax.set_aspect(_equal_aspect, adjustable='box')

    # ------------- legend ------------------
    if _show_legend:
        plt.legend(loc=_leg_loc,frameon=False,fontsize=_legfontsize,ncol=_leg_ncol)

    # ------------- grid ------------------
    if _show_grid:
        plt.grid(which='major',axis='both',linewidth=_gridlinewidth,color=_gridlinecolor,linestyle=_gridlinestyle)
        plt.grid(which='minor',axis='both',linewidth=_gridlinewidth,color=_gridlinecolor,linestyle=_gridlinestyle)        

def format_origin():
    """
    This routine formats the origin of the plot
    """ 
    def tick_formatter(x, pos):
        if x == 0.0:
            return '0'
        else:
            return '{:.1f}'.format(x)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(tick_formatter))

def gcontour(x,y,var,gsettings=gcontour_style()):
    """
    This routine plots the contour of a variable

    ---
    Example
    ---
    settings          = gcontour_style()      # get default settings \n               
    settings["title"] = '$u=\cos(x)\cos(y)$'  # add title            \n   
    gcontour(x_2d, y_2d, z_2d, settings)      # plot the curve       \n               
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
    _xtick_minor       = assign_value(_xtick_minor, (np.max(x)-np.min(x))/8) # 1 minor xtick between 2 major xticks
    _ytick_major       = assign_value(_ytick_major, (np.max(y)-np.min(y))/4) # 5 major yticks
    _ytick_minor       = assign_value(_ytick_minor, (np.max(y)-np.min(y))/8) # 1 minor ytick between 2 major yticks
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

def gtext(_text,_x,_y,_fontsize=22,_fontweight='normal',\
          _color='k',_rotation=0,_ha='left',_va='bottom',\
            _facecolor='white',_edgecolor='white'):
    """
    This routine is used to add a text
        - _text      : text
        - _x         : x position
        - _y         : y position
        - _fontsize  : font size
        - _fontweight: font weight
        - _color     : font color
        - _rotation  : rotation angle
        - _ha        : horizontal alignment
        - _va        : vertical alignment
        - _facecolor : face color
        - _edgecolor : edge color
    """
    plt.text(_x,_y,_text,fontsize=_fontsize,fontweight=_fontweight,\
             color=_color,rotation=_rotation,ha=_ha,va=_va, \
             bbox=dict(facecolor=_facecolor, edgecolor=_edgecolor))

def gsavefig(_filename,_figsize=None,_dpi=300,_format='png'):
    """
    This routine is used to save figure
    """
    if _figsize is None:
        _figsize = plt.gcf().get_size_inches()
    else:
        plt.gcf().set_size_inches(_figsize[0],_figsize[1])

    _filename_all = _filename + '.' + _format

    plt.savefig(fname=_filename_all,format=_format,dpi=_dpi,bbox_inches='tight',pad_inches=0.1)

def generate_new_cmap(cmap,num_colors=256):
    """
    This routine is used to generate a new colormap based on the original colormap
    """
    original_cmap = plt.get_cmap(cmap, 4)

    # Convert the ListedColormap to a LinearSegmentedColormap
    new_cmap = colors.LinearSegmentedColormap.from_list(
        name='new_cmap',
        colors=original_cmap(np.linspace(0, 1, original_cmap.N)),
    )

    # Interpolate the color data to increase the number of colors
    cdict = new_cmap._segmentdata
    new_cdict = {}
    for key in cdict.keys():
        data = np.array(cdict[key])
        new_data = np.zeros((num_colors, data.shape[1]))
        new_data[:, 0] = np.linspace(0, 1, num_colors)
        for i in range(1, data.shape[1]):
            new_data[:, i] = np.interp(new_data[:, 0], data[:, 0], data[:, i])
        new_cdict[key] = tuple(map(tuple, new_data))

    # Create a new colormap with the interpolated colors
    new_cmap = colors.LinearSegmentedColormap('new_cmap_enhanced', new_cdict)
    return new_cmap