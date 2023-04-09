
## About The Reposity

### Idea 

The idea of this reposity came from the ***Tecplot Macro language***, which is used to 
define the style of the plot in a `.lay` file. Take `DuctFlow.lay` for example (you can locate it at the folder `/examples/SimpleData` )

```C++
#!MC 1410
$!VarSet |LFDSFN1| = '"DuctFlow.plt"'
$!VarSet |LFDSVL1| = '"X(M)" "Y(M)" "Z(M)" "U(M/S)" "V(M/S)" "W(M/S)" "P(N/m2)" "T(K)"'
$!CreateColorMap 
  Name = 'Sequential - Viridis'
  NumControlPoints = 11
  ControlPoint 1
    {
    ColorMapFraction = 0
    LeadRGB
      {
      R = 68
      G = 1
      B = 84
      }
...    
$!FrameControl ActivateByNumber
  Frame = 1
```
The styles of the plot are defined with keys like `Name`, `NumControlPoints`, `LeadRGB` and so on. 
Hence, this approach is applied to my user-defined functions
`gplot()` and `gcontour()` with `gcontourline()`, which are used to plot curves and contours respectively. 

### Features 



## Getting Started

### Installation quick-start

Python libraries [numpy](https://numpy.org/), [matplotlib](https://matplotlib.org/) 
and [cmaps](https://github.com/hhuangwx/cmaps) are required to run the code. You can install them by running the following commands in your terminal (if installed, just skip).
FYI, the colormaps in `cmaps` are from [NCL](https://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml) website.
```
pip install matplotlib
pip install numpy
pip install cmaps
```

### Usage

The default style have been defined, which is elaborately designed for scientific visualization. And many other styles are also defined with 
`gplot_style_k()`, `gplot_style_r()` and so on.

add `lib_plot.py` to your working directory, and import it by
```python
from lib_plot import *
```

Then you can use the functions `gplot()` and `gcontour()` with `gcontourline()` to plot curves and contours respectively. For example, you can plot the following figure by running the following code.


some tips

- `gplot()` is a wrapper of `matplotlib.pyplot.plot()`, so you can use all the arguments of `matplotlib.pyplot.plot()` in `gplot()`.
- the default format of gsavefig() is .png, whose resolution is 300 dpi. '.eps', '.pdf' and '.svg' are also supported.


Further details are available in the .ipynb file.

#### Parameters

##### for gplot()

  - settings for curves
      - `color`          : color of the curve (choices: "k", "#D20000", "#2d2dff",'#00D200','#F97D01')
      - `linestyle`      : style of the curve (choices: "-", "--", "-.", ":")
      - `label`          : label of the curve, which will be shown in the legend
      - `zorder`         : zorder of the curve (the larger the value, the upper the curve)
      - `clip_on`        : clip the curves or not
  - settings for title
      - `title`          : title of the figure, which will be shown in the title
      - `titlefontsize`  : fontsize of the title
  - settings for markers
      - `marker`         : marker of the curve (choices: ["o", "s", "D", "v", "^", ">", "<")
      - `markerfacecolor`: set None to show hallow markers
  - settings for ticks
      - `xtick_major`    : major ticks of x
      - `xtick_minor`    : minor ticks of x
      - `ytick_major`    : major ticks of y
      - `ytick_minor`    : minor ticks of y
  - settings for x labels and y labels
      - `xlabel`         : x label          : set $x$ to show x in latex
      - `ylabel`         : y label          : set $y$ to show y in latex
      - `xlabelpad`      : blank padding of the x label
      - `ylabelpad`      : blank padding of the y label
      - `xrotation`      : rotation of the x label
      - `yrotation`      : rotation of the y label
  - settings for grids
      - `show_grid`      : show grid or not
      - `gridlinecolor`  : color of the grid line
      - `gridlinewidth`  : width of the grid line
      - `gridlinestyle`  : style of the grid line
  - settings for axis
      - `xmin`,`xmax`,`ymin`,`ymax`: range of x and y
      - `xscale`         : scale of the x axis (choices: ["linear", "log"])
      - `yscale`         : scale of the y axis (choices: ["linear", "log"])
      - `equal_aspect`   : set equal aspect or not
  - settings for legend
      - `leg_loc`        : location of the legend
      - `legfontsize`    : fontsize of the legend
      - `leg_ncol`       : number of columns of the legend

##### for gcontour()

- settings for contourf
    - `pcolor_contourf`: plot pcolormesh (default) or contourf (use 1 to activate)
    - `levels`: levels of the contourf
- settings for axis
    - `xmin`, `xmax`, `ymin`, `ymax`: range of x and y
    - `equal_aspect`: equal aspect or not
- settings for color
    - `vmin`: minimum value mapped to color
    - `vmax`: maximum value mapped to color
    - `cmap`: colormap
    - `alpha`: alpha of the contour
    - `shading`: shading of the contour
    - `antialiasing`: anti-aliasing or not
- settings for x label and y label
    - `xlabel`: x label: set $x$ to show x in latex
    - `ylabel`: y label: set $y$ to show y in latex
    - `xlabelpad`: labelpad of x label
    - `ylabelpad`: labelpad of y label
    - `xrotation`: angle of x label
    - `yrotation`: angle of y label
- settings for title
    - `title`: title of the contour
- settings for ticks    
    - `xtick_major`: major x ticks
    - `xtick_minor`: minor x ticks
    - `ytick_major`: major y ticks
    - `ytick_minor`: minor y ticks
- settings for colorbar
    - `show_colorbar`: show colorbar or not
    - `bar_num_ticks`: number of ticks in the colorbar
    - `bar_label`: label of the colorbar
    - `bar_tick_length`: length of the ticks in the colorbar
    - `bar_tick_width`: width of the ticks in the colorbar
    - `bar_orientation`: orientation of the colorbar
    - `bar_shrink`: shrink of the colorbar
    - `bar_position`: position of the colorbar
    - `bar_labelpad`: labelpad of the colorbar
- settings for grid
    - `show_grid`: show grid or not
    - `linecolor`: color of the grid
    - `linewidth`: width of the grid
    - `linestyle`: style of the grid




## Styles

### for gplot()

The only difference between the default style and the other styles is the color of the curve. 

- `gplot_style_k()`: black ('#000000')
- `gplot_style_r()`: red ('#D20000')
- `gplot_style_b()`: blue ('#2d2dff')
- `gplot_style_g()`: green ('#00D200')

FYI, the RGB values are obtained from ([Zhao & Sandberg, 2020](https://doi.org/10.1017/jfm.2020.39)).

### for gcontour()

The default style is the same as the default style of `gplot()`.


## Contact

- Email: yuchen.ge@stu.pku.edu.cn
- Github Page: https://github.com/GYC-lab
